import os

print(os.environ)

home_dir = os.environ['HOME']
print(home_dir)

# Only works if env as set:
# CUSTOM=hello python 03-environment.py
custom_env = os.environ['CUSTOM']
print(custom_env)
