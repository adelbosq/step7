(ns fizzbuzz)

(defn fizzbuzz [] 
  (let [natural-numbers (drop 1 (range))
        label           (fn [n]
                          (cond
                            (zero? (mod n 15)) "FizzBuzz"
                            (zero? (mod n 3)) "Fizz"
                            (zero? (mod n 5)) "Buzz"
                            :else n))]
    (map label natural-numbers)))

(take 100 (fizzbuzz))
