"""Task 5 - import cost of each organisation and sys.modules caching."""
import subprocess, sys, time

cases = {"(a) one script": ("a_one_script", "import attendance_app"),
         "(b) one module": ("b_module", "import attendance_lib"),
         "(c) three modules": ("c_three_modules", "import reader, stats, report"),
         "(d) package": ("d_package", "import attendance")}
for name, (folder, stmt) in cases.items():
    code = (f"import time,sys,tracemalloc;tracemalloc.start();t=time.perf_counter();{stmt};"
            f"t=time.perf_counter()-t;print(round(t*1e3,3),len([m for m in sys.modules if m in "
            f"('attendance_app','attendance_lib','reader','stats','report') or m.startswith('attendance')]),"
            f"tracemalloc.get_traced_memory()[1])")
    out = subprocess.run([sys.executable, "-c", code], cwd=folder, capture_output=True, text=True).stdout.split()
    print(f"{name:18}: first import {out[0]:>6} ms, modules loaded {out[1]}, memory {int(out[2]):>6} B")
sys.path.insert(0, "d_package")
t = time.perf_counter(); import attendance; t1 = time.perf_counter() - t
t = time.perf_counter(); import attendance; t2 = time.perf_counter() - t
print(f"package: first import {t1 * 1e3:.3f} ms, second import {t2 * 1e6:.2f} us (taken from sys.modules)")
