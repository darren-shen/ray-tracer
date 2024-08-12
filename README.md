Ray Tracer


This is an open-source ray tracing engine written in Python, designed for educational purposes and readability, with performance optimizations using Numpy. The engine supports complex materials like metal and glass and includes advanced features such as anti-aliasing and defocus blur.

Features
Complex Materials: Support for reflective materials like metal and refractive materials like glass.
Advanced Rendering Techniques: Includes anti-aliasing and defocus blur to produce smoother and more realistic images.
Performance Optimizations: Rendering speed improved by 200% through efficient sampling processes and matrix calculations.
Scene Customization: Easily customizable scenes with different objects, materials, and lighting setups.
Educational Purpose: Written in Python for readability, making it an excellent resource for learning the fundamentals of ray tracing.
Getting Started
Prerequisites
Python 3.8 or higher
Numpy
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/darren-shen/ray-tracer.git
cd ray-tracer
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Running the Ray Tracer
To render a scene, simply run the main.py script:

bash
Copy code
python main.py
This will output an image file (output.png) in the project directory, showcasing a scene with various objects and materials.

Customizing the Scene
The scene configuration can be modified in scene.py. You can add or remove objects, change their materials, or adjust the lighting and camera settings to create your unique scenes.

python
Copy code
# Example: Adding a new sphere to the scene
from objects import Sphere
from materials import Lambertian, Metal

# Create a new sphere
new_sphere = Sphere(center=[0, -1, -3], radius=1, material=Metal(albedo=[0.8, 0.6, 0.2], fuzz=0.3))

# Add it to the scene
scene_objects.append(new_sphere)
Performance Optimization
The engine has been optimized for performance using Numpy. However, due to Python’s inherent limitations, the engine may not be as fast as implementations in lower-level languages like C++. If you need even better performance, consider implementing critical parts in Cython or using parallel processing techniques.

Sample Renders
Here are some example images rendered using this engine:




Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

Fork the repository
Create a new branch (git checkout -b feature-branch)
Commit your changes (git commit -m 'Add some feature')
Push to the branch (git push origin feature-branch)
Open a pull request
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
This project was inspired by Peter Shirley's "Ray Tracing in One Weekend" series, which provides a great introduction to the concepts behind ray tracing.

Feel free to adjust any details to better fit your project or preferences!
