<style>
    .dim {
        color: gray;
    }
</style>

# BACKLOG

## Planned updates
### • Toolkit for *mean* and *standard deviation*
Add toolkit for studying CI methods for other statistics as well, such as *mean*, *standard deviation*, etc.



## Optional updates / suggestions

### • Improve optimization for analytical computation of coverage for CI methods for *proportions* and for *difference between two proportions*
Try not using `z_precision` at all. Instead, loop through `covered` list, which is `0`s and `1`s, and figure out the minimal range that includes all `1`s (the range starting from the first `1` and to the last `1`). This way it will cover 100% of important binomial distribution and will provide true 100% precision for the calculation. But see if it provides faster execution.
 <span class="dim">Also, my guess is that this range starts with the first `1` and ends right before the first `0` after that. But who knows.</span>


