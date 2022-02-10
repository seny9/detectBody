from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
import sys
sys.path.insert(1, '../')
import pykinect_azure as pykinect
		

if __name__ == "__main__":


	# Initialize the library, if the library is not found, add the library path as argument
	pykinect.initialize_libraries(track_body=True)

	# Modify camera configuration
	device_config = pykinect.default_configuration
	device_config.color_format = pykinect.K4A_IMAGE_FORMAT_COLOR_BGRA32
	device_config.color_resolution = pykinect.K4A_COLOR_RESOLUTION_720P
	device_config.depth_mode = pykinect.K4A_DEPTH_MODE_WFOV_2X2BINNED
	
	# Start device
	device = pykinect.start_device(config=device_config)
	# Start body tracker
	bodyTracker = pykinect.start_body_tracker()

	cv2.namedWindow('Image',cv2.WINDOW_NORMAL)
	while True:

		# Get capture
		capture = device.update()

		# Get body tracker frame
		body_frame = bodyTracker.update()

		# Get the color depth image from the capture
		ret, depth_color_image = capture.get_colored_depth_image()

		# Get the colored body segmentation
		ret, body_image_color = body_frame.get_segmentation_image()

		if not ret:
			continue
			
		# Get the colored depth
		ret, transformed_colored_depth_image = capture.get_transformed_colored_depth_image()

		# Combine both images
		combined_image = cv2.addWeighted(depth_color_image, 0.6, body_image_color, 0.4, 0)

		# Draw the skeletons
		combined_image = body_frame.draw_bodies(combined_image)

		cv2.imshow('Image',combined_image)
		
		# Press q key to stop
		if cv2.waitKey(1) == ord('q'):  
			break
		

	