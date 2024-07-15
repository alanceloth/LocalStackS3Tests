import concurrent.futures
import subprocess
import time

def run_script(script_name):
    start_time = time.time()
    result = subprocess.run(['poetry', 'run', 'python', script_name], capture_output=True, text=True)
    end_time = time.time()
    return script_name, end_time - start_time, result.stdout, result.stderr

if __name__ == "__main__":
    scripts = ["app/source/functions/data_generate_pandas.py", "app/source/functions/data_generate_polars.py"]
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(run_script, script) for script in scripts]
        
        for future in concurrent.futures.as_completed(futures):
            script_name, duration, stdout, stderr = future.result()
            print(f"{script_name} terminou em {duration:.2f} segundos")
            print(f"Saída:\n{stdout}")
            if stderr:
                print(f"Erros:\n{stderr}")
