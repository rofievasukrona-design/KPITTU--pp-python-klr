def analyze(*datasets, **options):     
    merge = options.get('merge', False)     
    normalize = options.get('normalize', False)     
    rnd = options.get('round', None)          
    
    def calc_mean(data):         
        return sum(data) / len(data)          
    
    def calc_median(data):         
        data = sorted(data)         
        n = len(data)         
        mid = n // 2         
        if n % 2 == 1:             
            return data[mid]         
        else:             
            return (data[mid] + data[mid]) / 2              
        
    def normalize_data(data):         
        mn, mx = min(data), max(data)         
        if mn == mx:             
            return [0 for _ in data]         
        return [(x - mn) / (mx - mn) for x in data]              
    
    def calc_stats(data):         
        if not data:              
            return {                
                 'sum': 0,                  
                 'mean': None,                  
                 'median': None              
                 }                  
        
        return { 
            'sum' : sum(data),             
            'mean': calc_mean(data),              
            'median': calc_median(data),             
            }                  
        
    results = {}              
        
    if merge:         
        merged = [x for ds in datasets for x in ds]         
        if normalize:             
            merged = normalize_data(merged)         
        stats = calc_stats(merged)                          
        
        if rnd is not None:             
            stats = {k: round(v, rnd) for k, v in stats.items()}                          
            
        return {'merged': stats}                  
    
    for i, ds in enumerate(datasets, 1):         
        data = ds         
        if normalize:             
            data = normalize_data(data)         
            
        stats = calc_stats(data)                          
        if rnd is not None:             
            stats = {k: round(v, rnd) for k, v in stats.items()}                              
            
        results[f"dataset_{i}"] = stats                       
        
    return results          

print(analyze([5, 5, 5], normalize = True))