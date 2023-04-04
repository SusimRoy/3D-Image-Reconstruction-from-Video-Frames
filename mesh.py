# python3 -m pip install open3d


import matplotlib.pyplot as plt
import numpy as np
import open3d as o3d

def stitch_point_clouds(pcd1, pcd2):
    # Create instance of ICP registration class
    icp = o3d.pipelines.registration.registration_icp(
        pcd1, pcd2, max_correspondence_distance=0.05)

    # Apply transformation matrix to pcd2
    pcd2.transform(icp.transformation)

    # Combine pcd1 and transformed pcd2
    pcd_combined = pcd1 + pcd2

    # Return the combined point cloud
    return pcd_combined


def creator(pcd1_points,pcd2_points):


    fig = plt.figure()

    pcd1_colors = np.array([
        [0.0, 0.0, 1.0],
        [0.0, 0.0, 1.0],
        [0.0, 0.0, 1.0],
        [0.0, 0.0, 1.0],
        [0.0, 0.0, 1.0],
        [0.0, 0.0, 1.0],
        [0.0, 0.0, 1.0]
    ])
    pcd1 = o3d.geometry.PointCloud()
    pcd1.points = o3d.utility.Vector3dVector(pcd1_points)
    pcd1.colors = o3d.utility.Vector3dVector(pcd1_colors)

    # Create second point cloud with incomplete points

    pcd2_colors = np.array([
        [1.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
        [1.0, 0.0, 0.0]
    ])
    pcd2 = o3d.geometry.PointCloud()
    pcd2.points = o3d.utility.Vector3dVector(pcd2_points)
    pcd2.colors = o3d.utility.Vector3dVector(pcd2_colors)

    # Create point cloud with geometric shapes
    sphere = o3d.geometry.TriangleMesh.create_sphere(radius=0.5)
    sphere.paint_uniform_color([1.0, 0.0, 0.0])
    sphere.translate([-1.0, 0.0, 0.0])

    box = o3d.geometry.TriangleMesh.create_box(width=1.0, height=1.0, depth=1.0)
    box.paint_uniform_color([0.0, 1.0, 0.0])
    box.translate([0.0, 0.0, 0.0])

    cylinder = o3d.geometry.TriangleMesh.create_cylinder(radius=0.5, height=1.0)
    cylinder.paint_uniform_color([0.0, 0.0, 1.0])
    cylinder.translate([1.0, 0.0, 0.0])

    # Register and combine the two point clouds
    pcd_combined = stitch_point_clouds(pcd1, pcd2)

    points = np.asarray(pcd_combined.points)
    colors = np.asarray(pcd_combined.colors)

    # Visualize the combined point cloud
    import plotly.graph_objects as go

    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=points[:,0], y=points[:,1], z=points[:,2], 
                mode='markers',
                marker=dict(size=1, color=colors)
            )
        ],
        layout=dict(
            scene=dict(
                xaxis=dict(visible=False),
                yaxis=dict(visible=False),
                zaxis=dict(visible=False)
            )
        )
    )
    fig.show()