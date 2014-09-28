dict(description='For debugging',
           data_dir='../data/debug/',
           max_depth=10,
           random_order=False,
           k=1,
           debug=False,
           n_rand=3,
           sd=2, 
           jitter_sd=0.1,
           verbose=False,
           make_predictions=False,
           skip_complete=False,
           results_dir='../results/debug/',
           iters=250,
           base_kernels='SE,Noise',
           random_seed=1,
           period_heuristic=3,
           max_period_heuristic=5,
           period_heuristic_type='min',
           subset=False,
           bundle_size=10,
           additive_form=True,
           mean='ff.MeanZero()',      # Starting mean
           kernel='ff.NoiseKernel()', # Starting kernel
           lik='ff.LikGauss(sf=-np.Inf)', # Starting likelihood
           score='bic',
           stopping_criteria=['no_improvement'],
           improvement_tolerance=0.01,
           search_operators=[('A', ('+', 'A', 'B'), {'A': 'kernel', 'B': 'base'}),
                             ('A', ('*', 'A', 'B'), {'A': 'kernel', 'B': 'base-not-const'}),
                             ('A', 'B', {'A': 'kernel', 'B': 'base'}),
                             ('A', ('None',), {'A': 'kernel'})])
