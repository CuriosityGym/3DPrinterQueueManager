$(document).ready(function(){		
			
			if ( WEBGL.isWebGLAvailable() === false ) {
				document.getElementById("3DViewer").appendChild( WEBGL.getWebGLErrorMessage() );
			}
			var camera, controls, scene, renderer;
			var width=400;
			var height=400;
			init();
			//render(); // remove when using next line for animation loop (requestAnimationFrame)
			animate();
			function init() {
				scene = new THREE.Scene();
				scene.background = new THREE.Color( 0xcccccc );
				//scene.fog = new THREE.FogExp2( 0xcccccc, 0.002 );
				renderer = new THREE.WebGLRenderer( { antialias: true } );
				renderer.setPixelRatio( window.devicePixelRatio );
				renderer.setSize( width, height );
				document.getElementById("3DViewer").appendChild( renderer.domElement );
				camera = new THREE.PerspectiveCamera( 10, width/height, 1, 1000 );
				camera.position.set(0,0,0);
				//camera.position.z = -10
				// controls
				controls = new THREE.OrbitControls( camera, renderer.domElement );
				//controls.addEventListener( 'change', render ); // call this only in static scenes (i.e., if there is no animation loop)
				controls.enableDamping = true; // an animation loop is required when either damping or auto-rotation are enabled
				controls.dampingFactor = 0.25;
				controls.screenSpacePanning = false;
				controls.minDistance = 15;
				controls.maxDistance = 1000;				
				controls.rotateSpeed = 2.0
				controls.zoomSpeed = 5
				controls.panSpeed = 2
				controls.enableZoom = true
				// world
				
				
				
				var loader = new THREE.STLLoader();
				filePath=returnSTLPath();
				loader.load( filePath, function ( geometry ) {					

					var material = new THREE.MeshPhongMaterial( { color: 0x2689a7, specular: 0x111111, shininess: 2 } );
					var mesh = new THREE.Mesh( geometry, material );

					mesh.position.set( 0, 0, 0 );
					mesh.rotation.set( 0, 0, 0 );
					mesh.scale.set( 0.2,0.2,0.2 );

					//mesh.castShadow = true;
					//mesh.receiveShadow = true;

					scene.add( mesh );

				} );
				// lights
				var light = new THREE.DirectionalLight( 0xffffff );
				light.position.set( 1, 1, 1 );
				scene.add( light );
				var light = new THREE.DirectionalLight( 0x002288 );
				light.position.set( - 1, - 1, - 1 );
				scene.add( light );
				var light = new THREE.AmbientLight( 0x222222 );
				scene.add( light );
				//
				window.addEventListener( 'resize', onWindowResize, false );
			}
			function onWindowResize() {
				camera.aspect = width/height;
				camera.updateProjectionMatrix();
				scaling=window.innerWidth/window.innerHeight;
				renderer.setSize( width*scaling, height*scaling );
			}
			function animate() {
				requestAnimationFrame( animate );
				controls.update(); // only required if controls.enableDamping = true, or if controls.autoRotate = true
				render();
			}
			function render() {
				renderer.render( scene, camera );
			}
			
});				