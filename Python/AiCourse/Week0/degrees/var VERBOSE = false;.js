var VERBOSE = false;
 
var log = function() {
    if (!VERBOSE) {
        return;
    }
    console.log.apply(null, arguments);
}
 
 
var TickChallenge = function() {
    this.interval = null;
    this.period = 1000; // ms
}
 
 
TickChallenge.prototype.start = function() {
    if (this.interval !== null) {
        clearInterval(this.interval);
    }
 
    this.interval = setInterval(this.oneTick.bind(this), this.period);
};
 
TickChallenge.prototype.stop = function() {
    if (this.interval !== null) {
        clearInterval(this.interval);
    }
};
 
 
TickChallenge.prototype.oneTick = function() {
    var maxTier = this.getTiers();
 
    // max out the top dimension to keep the prices spaced.
    while (buyManyDimension(maxTier)) {}
    log("max tier", maxTier);
 
    // TODO should this be >0 or >=0? (i.e. does game 0 index or 1 index)
    // loop backwards
    for (var tier = maxTier - 1; tier > 0; tier--) {
        // buy this dimension until we can't buy anymore, or the price would catch up to the
        // next tier's price
        while (this.getNextPrice(tier).lessThan(this.getCurrentPrice(tier + 1))) {
            var buyResult = buyManyDimension(tier);
            if (!buyResult) {
                log("breaking due to !buyResult on tier", tier);
                break;
            }
        }
        log("finishing tier", tier);
    }
 
    // buy tick upgrades
    var lastTier = tier + 1; // this is the last tier we purchased, i.e. the first tier. I still don't know if we're 0 or 1 indexing ¯\_(ツ)_/¯
    log("last tier", lastTier);
    while ( (this.getNextTickPrice().lessThan(this.getCurrentPrice(lastTier)))
             && buyTickSpeed()) {}
};
 
TickChallenge.prototype.getNextTickPrice = function() {
    return player.tickSpeedCost.times(player.tickspeedMultiplier);
}
 
TickChallenge.prototype.getNextPrice = function(tier) {
    var currentPrice = this.getCurrentPrice(tier);
    multiplier = getDimensionCostMultiplier(tier);
    return currentPrice.times(multiplier);
};
 
TickChallenge.prototype.getCurrentPrice = function(tier) {
    var name = TIER_NAMES[tier];
    var cost = player[name + 'Cost'].times(10);
    return cost;
};
 
 
TickChallenge.prototype.getTiers = function() {
    var i = 1;
    while (canBuyDimension(i)) {
        i++;
    }
 
    var maxCanBuy = i - 1;
    // 9 says it can be bought, but buyManyDimension(9) fails?
    if (maxCanBuy > 8) {
        return 8;
    }
 
    return maxCanBuy;
};
 
var t = new TickChallenge();
t.start();