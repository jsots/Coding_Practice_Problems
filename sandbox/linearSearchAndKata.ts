export function linear_search(haystack: number[], needle: number): boolean {
    for (let i = 0; i < haystack.length; ++i) {
        if (haystack[i] === needle) {
            return true
        }
    }
}

export function bs_list(haystack: number[], needle: number): boolean {
    let lo = 0;
    let hi = haystack.length
    do {
        const m = Math.floor(lo + (hi - lo) / 2);
        const v = haystack[m];

        if (v === needle) {
            return true;
        } else if (v > needle) {
            hi = m;
        } else {
            lo = m +1;
        }

    } while (lo < hi);

    return false;
}

export function two_crystal_balls(breaks: boolean[]): number {
    const jmpAmount = Math.floor(Math.sqrt(breaks.length));

    // Using sqrt will allow for a function that has a better run time than just a linear one. This will be root N big O
    let i = jmpAmount;
    for (; i < breaks.length; i += jmpAmount) {
        if (breaks[i]) {
            break;
        }
    }

    i -= jmpAmount;

    for (let j = 0; j < jmpAmount && i < breaks.length; ++j, ++i) {
        if (breaks[i]) {
            return i;
        }
    }

    return -1;
}


export bubble_sort(arr: number[]): void {
    for (let i = 0; i < arr.length; ++i) {
        for (let j = 0; j < arr.length - 1 - i; ++j) {

            if (arr[j] > arr[j + 1]) {
                const tmp = arr[j];
                arr[j] = arr[j+1];
                arr[j + 1] = tmp;
            }
        }
    }
}