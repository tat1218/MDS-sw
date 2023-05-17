for algo in "HEFT" "CPOP" "PEFT" "DHS"
do
  for services in 3
  do
    for mu in 0.05
    do
      for sig in 0.05
      do
        for t in {1..1000}
        do
          echo "auto test - server: ${algo} service: ${services} mu: ${mu} sig: ${sig}"
          python3 main.py --num_servers=4 --num_services=$services --offloading=$algo --mu $mu --sig $sig --random_test True >> result.txt
        done
      done
    done
  done
done