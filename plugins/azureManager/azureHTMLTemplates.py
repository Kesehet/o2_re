def create_vm_step_1(next_url:str):
    return '''
<!DOCTYPE html>
<html>
<head>
	<title>Create A POP</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"  />
	<style>
		#canvas{
            height: 100vh;
            margin-left: 10%;
        }
        .two-line-ellipsis {
            overflow: hidden;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
        }
        .w3-light-grey, .w3-hover-light-grey:hover, .w3-light-gray, .w3-hover-light-gray:hover {
            color: #313946 !important;
            background-color: #f1f1f1 !important;
        }
        /* Hide scrollbar for Chrome, Safari and Opera */
        #optimalBox::-webkit-scrollbar {
        display: none;
        }

        /* Hide scrollbar for IE, Edge and Firefox */
        #optimalBox {
        height: 40vh;
        -ms-overflow-style: none;  /* IE and Edge */
        scrollbar-width: none;  /* Firefox */
        }
        #optimalBox:hover{
            height: 60vh;
        }
	</style>
</head>
<body class="w3-animate-opacity" style="overflow-x: hidden;">
    <div class="w3-row">
        <div class="w3-container w3-padding-large w3-third publicSans" >
            <div class="w3-container">
                <h1 class="publicSans" style="font-weight: bold;"> Create a new Point Of Presence </h1>
                <h6 class="publicSans" style="font-weight: 100;">Unleash the power of the cloud with a new POP in a location of your choice. Create and host your VM with seamless ease and flexibility, and take your digital world to new heights.</h6>
            </div>
            <div class="w3-container publicSans" id="board" style="display: none;">
                    <h2 class="blueText w3-padding" id="board_name">City, Country</h2>
                    <div class="" style="padding-left: 32px;">
                        <h4 id="board_continent" class="blue" >Continent</h4>
                        <p id="board_desc" style="font-weight: 100;margin-top: -8px;margin-left: 16px;">Nestled in the heart of the bustling city, our Point of Presence (POP) location is the perfect choice for businesses that demand high-performance cloud services. Located in a state-of-the-art data center, this POP offers lightning-fast connectivity and low-latency networking, ensuring that your applications and services run smoothly and efficiently. With multiple redundant connections and backup power supplies, this POP is designed for maximum uptime and reliability, giving you the peace of mind to focus on growing your business. Our expert team of engineers and support staff are on-hand 24/7 to ensure that your cloud services are always running at peak performance. Choose our POP location for the ultimate in cloud computing performance and reliability.</p>
                        <div id="next_button" class="publicSans heavyFont w3-margin w3-button w3-border w3-hover-white blue w3-round w3-right " >Next</div>
                    </div>
                    
            </div>
            <div id="unboard" class="w3-hide-small w3-container w3-animate-opacity w3-light-grey blackText publicSans w3-col l12 m12 s12 dashBorder w3-padding-large w3-center">
                <a href = "#canvas">
                    <div class="w3-container w3-xxxlarge blueText">
                        <i class="fas fa-map-marker"></i>
                    </div>
                    Select the Point of Presence (POP) of your choice by clicking on any of the markers on the globe.
                </a>
            </div>
            <div class="w3-container w3-padding">
                <h1 style="text-align: left;font-size: 2vw;"  >
                    <i class="fas fa-circle w3-small"></i>&nbsp;<i class="fas fa-circle w3-small"></i>&nbsp;<i class="fas fa-circle w3-small"></i>&nbsp;<i class="fas fa-circle w3-small"></i>
                </h1>
                
                <div class="w3-container w3-stretch">
                    <h3 class="bold" >Optimal points of presence</h3>
                </div>
                
                <div id="optimalBox" class="w3-container w3-stretch" style=" overflow-y: scroll;  -webkit-mask-image: linear-gradient(180deg, #000 90%, transparent);">

                </div>
            </div>
        </div>
        
        <div class="w3-hide-small w3-container w3-twothird w3-padding-large" style="overflow-x: hidden;">
            <div class=" " id="container">
                <canvas id="canvas">
            </div>
        </div>
        
    </div>
	
    <script>
        var addMark = undefined;
        MARKERS = [];
        const GLOBE_RADIUS = 3;
        const Colors = {"black":"#313946","blue":"#2288E6","shine":"#ef2475"}
        function addPoint(lat,long,col,data){
            addMark(getSpherePosition(lat,long,GLOBE_RADIUS),col,data)
        }
        function setBoard(name,place,desc){
            document.getElementById("unboard").style.display = "none";
            document.getElementById("board").style.display = "";
            document.getElementById("board_name").innerHTML = name;
            document.getElementById("board_continent").innerHTML = place;
            document.getElementById("board_desc").innerHTML = desc;
            document.getElementById("next_button").style.display = "";
            if(name == ""){
                document.getElementById("next_button").style.display = "none";
                document.getElementById("unboard").style.display = "";
                
            }
        }
        document.getElementById("next_button").addEventListener("click",()=>{
            var next_url = "'''+next_url+'''".replace("[*data*]",JSON.stringify(FOCUS_MARKER.userData));
            window.location.href = next_url;
        })

        function setOptimalList(){
            var optimalDiv = document.getElementById("optimalBox")
            for(var i = 0 ; i < MARKERS.length; i++){
                optimalDiv.innerHTML += optimalBox(MARKERS[i].userData.cityName,MARKERS[i].userData.desc,i);
            }
        }
        function markerIDSetter(id){
            var i = MARKERS[id];
            setBoard(i.userData.cityName,i.userData.place,i.userData.desc);
            
            FOCUS_MARKER = MARKERS[id];
            INTERSECTED = MARKERS[id];
            
        }
        function loadLocations() {
            var dat = JSON.parse(this.responseText.replaceAll("&#39;",'"').replaceAll("&#34;",'"').replaceAll("'",'"'));
            console.log(dat)
            for(var i = 0 ; i < dat.length;i++){
                var d = dat[i];
                addPoint(d.lat,d.long,"#1fb2d0",{"cityName":d.fullName,"place":d.name2,desc:d.desc})
            }
            setOptimalList();
        }

        

        function optimalBox(name,desc,MARKER_ID){
            return `<div class="w3-container w3-padding w3-tooltip">
                        <div class="w3-col l12 m12 s12 w3-padding w3-hover-light-grey w3-round w3-large w3-animate-right blueText w3-card-2" >
                            <div class="w3-col l1 m1 s1 w3-xxlarge w3-padding-large" style="padding-right: 16px;">
                                <i class="fas fa-map-marker-alt"></i>
                            </div>
                            <div class="w3-col l11 m11 s11" style="padding-left: 16px;text-align: left;">
                                `+name+`
                                <p class="lightFont blackText w3-small two-line-ellipsis" >`+desc+`</p>
                                <div class="w3-text publicSans heavyFont w3-margin w3-button w3-border w3-hover-white blue w3-round w3-right" onclick="markerIDSetter(`+MARKER_ID+`)">Select</div>
                            </div>
                        </div>  
                    </div>`;
        }
        function getSpherePosition(latitude, longitude, radius) {
            // Convert latitude and longitude from degrees to radians
            var latRad = latitude * Math.PI / 180;
            var longRad = longitude * Math.PI / 180;

            // Calculate the x, y, and z coordinates of the point on the sphere
            var x = radius * Math.cos(latRad) * Math.cos(longRad);
            var y = radius * Math.sin(latRad);
            var z = radius * Math.cos(latRad) * Math.sin(longRad);

            // Return the 3D coordinate as a three.js Vector3 object
            return {"x":z,"y": y,"z": x};
        }
        window.addEventListener("load", (event) =>{
            document.getElementsByTagName("canvas")[0].style.position = "relative";
            const req = new XMLHttpRequest();
            req.addEventListener("load", loadLocations);
            req.open("GET", "https://control.3duverse.com/api/azure_open_api/main?task=get-machine-by-location");
            req.send();
            
        });

        var FOCUS_MARKER = undefined;
        var INTERSECTED;
    </script>
    <script src="https://code.createjs.com/1.0.0/tweenjs.min.js"></script>
	<script type="module">
        import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.124/build/three.module.js';
        import { OrbitControls } from 'https://cdn.jsdelivr.net/npm/three@0.124/examples/jsm/controls/OrbitControls.js';
       

        var canvas = document.getElementById('canvas');
        var parentElement = canvas.parentElement;
        
        var scene = new THREE.Scene();
        var camera = new THREE.PerspectiveCamera(75, parentElement.clientWidth / parentElement.clientHeight, 0.1, 100);
        camera.position.set(0, 0, (GLOBE_RADIUS*1.7));
        
        

        var renderer = new THREE.WebGLRenderer({ alpha: true, canvas: canvas });
        renderer.setSize(parentElement.clientWidth, parentElement.clientHeight);

        var globeGeometry = new THREE.SphereGeometry(GLOBE_RADIUS, 32, 32);
        var globeMaterial = new THREE.MeshBasicMaterial({ color: Colors.black, wireframe: true });
        var globeMesh = new THREE.Mesh(globeGeometry, globeMaterial);
        scene.add(globeMesh);

        function addMarker(pos, color,data) {
            var mrkerGeometry = new THREE.SphereGeometry(0.05, 16, 16);
            var mrkerMaterial = new THREE.MeshBasicMaterial({ color: color });
            var mrkerMesh = new THREE.Mesh(mrkerGeometry, mrkerMaterial);
            mrkerMesh.position.set(pos.x, pos.y, pos.z);
            mrkerMesh.userData = data;
            globeMesh.add(mrkerMesh);
            MARKERS.push(mrkerMesh);
        }
        addMark = addMarker;

        var controls = new OrbitControls(camera, renderer.domElement);
        controls.autoRotate = true
        controls.autoRotateSpeed = 0.5
        var raycaster = new THREE.Raycaster();
        var mouse = new THREE.Vector2();
        

        function onMouseMove(event) {
            var rect = canvas.getBoundingClientRect();
            mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
            mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;
        }

        function onDocumentMouseDown(event) {
            if (INTERSECTED) {
                
                
                console.log(camera.position);
                console.log(camera.rotation);
                var rotateToCam = INTERSECTED.userData.camera;
                FOCUS_MARKER = INTERSECTED;
            }
            else{
                FOCUS_MARKER = undefined;
            }
        }

        function cameraFocus(target,distance){
            
                const direction = new THREE.Vector3().subVectors(target, camera.position).normalize();
                const targetPosition = new THREE.Vector3().copy(target).add(direction.multiplyScalar(distance));
                camera.position.copy(targetPosition);

        }

        canvas.addEventListener('mousemove', onMouseMove, false);
        canvas.addEventListener('click', onDocumentMouseDown, false);

        function render() {
            requestAnimationFrame(render);

            raycaster.setFromCamera(mouse, camera);

            var intersects = raycaster.intersectObjects(globeMesh.children);
            
            if (intersects.length > 0) {
                if (INTERSECTED != intersects[0].object) {
                if (INTERSECTED) INTERSECTED.material.color.set(Colors.blue);
                INTERSECTED = intersects[0].object;
                INTERSECTED.material.color.set(Colors.black);
                }
            } else {
                if (INTERSECTED) INTERSECTED.material.color.set(Colors.blue);
                INTERSECTED = null;
            }
            
            
                


            if(INTERSECTED) {
                if(FOCUS_MARKER == undefined){
                    setBoard(INTERSECTED.userData.cityName,INTERSECTED.userData.place,INTERSECTED.userData.desc);
                    
                }
                else{
                    setBoard(FOCUS_MARKER.userData.cityName,FOCUS_MARKER.userData.place,FOCUS_MARKER.userData.desc)
                }
                controls.autoRotate = false;
            }
            else {
                if(FOCUS_MARKER != undefined){
                    controls.autoRotate = false;
                }
                else{
                    controls.autoRotate = true;
                    FOCUS_MARKER = undefined;
                    setBoard("","","")
                }
            }
            controls.update();
            renderer.render(scene, camera);
        }


        setInterval(()=>{
            var r1 = randomInteger(0,globeMesh.children.length-1);
            for (let i = 0; i < globeMesh.children.length; i++) {
                if(i != r1 && globeMesh.children[i] != FOCUS_MARKER){
                    globeMesh.children[i].material.color.set(Colors.shine);
                    setTimeout(()=>{
                        globeMesh.children[i].material.color.set(Colors.blue);
                    },1000)
                }
            }
            if(FOCUS_MARKER != undefined) {
                FOCUS_MARKER.material.color.set("#ff0000");
                //FOCUS_MARKER.scale.set(new THREE.Vector3(2,2,2));
            }
        },1000);
        render();

	</script>
    <script>
        function randomInteger(min, max) {
            return Math.floor(Math.random() * (max - min + 1)) + min;
        }
    </script>
</body>
</html>

    '''

def create_vm_step_2(next_url:str,data:dict):
    data["descr"] = ""
    return '''
<div class="w3-container w3-animate-opacity publicSans w3-padding-large" style="overflow-x: hidden;">
    <div class="w3-container w3-padding">
        <div class="w3-col l6 m8 s12">
            <h1 class="bold publicSans">Machine Type</h1>
            <h6 class="publicSans" style="font-weight: 100;" >Virtual Machines (VMs) are simulated computers that run within another physical machine. They allow you to run multiple operating systems on a single physical machine. VMs are categorized into Basic, Standard, and Premium based on their processing power and memory capacity. To choose the right VM for your needs, consider your workload, expected traffic, and application requirements. Opt for a Basic VM for light workloads, a Standard VM for moderate workloads, and a Premium VM for demanding workloads.</h6>
        </div>  
        <div class="w3-col l9 m8 w3-hide-small">

        </div>
    </div>
    <div id="guide1" class="w3-container w3-animate-bottom w3-center publicSans blackText " style="display: none;">
        <h1 class="">Please select a VM Type.</h1>
    </div>
    
    <div class = "w3-container" style="margin-top:8vh;">

        
        <div class="w3-container l4 m6 s12 w3-round boxPad w3-col w3-center "   >
            <div data-level="Basic" class="w3-container w3-padding w3-hover-light-gray w3-animate-left" onclick="selected(this,'Basic');">
                <i class="fas fa-hdd icon w3-ul"></i>
                <h3 class="" style="font-weight: 500;" >Basic</h3>
                <div class="w3-container">
                    <p class="blue w3-round  lightFont w3-padding" style="font-weight: 600;">Affordable VMs with basic computing power, suitable for simple workloads.</p>
                    <p class="w3-padding blackText lightFont">Our Basic category is perfect for small workloads and light usage scenarios. With up to 1 vCPU and 4 GB of RAM, you can run basic applications and perform light computing tasks with ease. The most important factor to consider when choosing Basic is cost-effectiveness.</p>                
                    <div class="w3-container" >
                        <table style="width: 100%;">
                            <tr class="blackText"><td><i class="fas fa-microchip"></i></td><td> Up to 1 vCPU</td></tr>
                            <tr class="blackText"><td><i class="fas fa-memory"></i></td><td> Up to 4 GB RAM</td></tr>
                            <tr class="blackText"><td><i class="fas fa-warehouse"></i></td><td> Up to 32 GB Storage</td></tr>
                            
                        </table>
                    </div>
                </div>
            </div>
        </div>


        <div class="w3-container l4 m6 s12 w3-round boxPad w3-col w3-center "  >
            <div data-level="Standard" class="w3-container w3-padding w3-hover-light-gray  w3-animate-bottom" onclick="selected(this,'Standard');">
              <i class="fas fa-server icon w3-ul"></i>
              <h3 class="" style="font-weight: 500;" >Standard</h3>
                <div class="w3-container">
                    <p class="blue w3-round  w3-padding " style="font-weight: 600;" >Balanced VMs with moderate computing power, suitable for most workloads.</p>
                    <p class="blackText w3-padding lightFont">Our Standard category is ideal for medium to heavy workloads. With up to 4 vCPUs and 16 GB of RAM, you can run multiple applications and perform more demanding computing tasks with ease. The most important factor to consider when choosing Standard is the balance between performance and cost.</p>
                    
                    <div class="w3-container" >
                        <table style="width: 100%;">
                            <tr class="blackText"><td><i class="fas fa-microchip"></i></td><td> Up to 8 vCPU</td></tr>
                            <tr class="blackText"><td><i class="fas fa-memory"></i></td><td> Up to 16 GB RAM</td></tr>
                            <tr class="blackText"><td><i class="fas fa-warehouse"></i></td><td> Up to 256 GB Storage</td></tr>
                            
                        </table>
                        
                    </div>
                </div>
            </div>
        </div>
  

            <div class="w3-container l4 m6 s12 w3-round boxPad w3-col w3-center"  >
                <div data-level="Premium" class="w3-container w3-padding w3-hover-light-gray w3-animate-right" onclick="selected(this,'Premium');">
                    <svg style="height: 15vh;" class="blackText" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Pro 6.3.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path fill="#cad1df" d="M448 32c-83.3 11-166.8 22-250 33-92 12.5-163.3 86.7-169 180-3.3 55.5 18 109.5 57.8 148.2L0 480c83.3-11 166.5-22 249.8-33 91.8-12.5 163.3-86.8 168.7-179.8 3.5-55.5-18-109.5-57.7-148.2L448 32zm-79.7 232.3c-4.2 79.5-74 139.2-152.8 134.5-79.5-4.7-140.7-71-136.3-151 4.5-79.2 74.3-139.3 153-134.5 79.3 4.7 140.5 71 136.1 151z"/></svg>
                    
                    <h3 class="" style="font-weight: 500;" >Premium</h3>
                    <div class="w3-container w3-tooltip ">
                        <p class="blue w3-round  w3-padding lightFont" style="font-weight: 600;">High-performance VMs with advanced computing power, suitable for demanding workloads.</p>
                        <p class="blackText w3-padding lightFont">Our Premium virtual machines are designed for businesses with high-performance needs, such as large databases, high-performance computing, and machine learning workloads. With up to 64 vCPUs and 256 GB of RAM, Premium VMs offer the highest levels of performance and reliability.</p>
                        <div class="w3-container" style="">
                            <table style="width: 100%;">
                                <tr class="blackText"><td><i class="fas fa-microchip"></i></td><td> Up to 64 vCPU</td></tr>
                                <tr class="blackText"><td><i class="fas fa-memory"></i></td><td> Up to 256 GB RAM</td></tr>
                                <tr class="blackText"><td><i class="fas fa-warehouse"></i></td><td> Up to 1 TB Storage</td></tr>
                                
                            </table>
                            
                        </div>
                    </div>
                </div>
            </div>    
    </div>
	<div class="w3-container w3-padding-large w3-center w3-animate-opacity w3-margin-large " style="margin-top: 2vh;">
        <div class="blue w3-button w3-left w3-round w3-large" ><a>< Back</a></div>
        <div class="blueText w3-button w3-center w3-round w3-large " ><a>Go Custom !</a></div>
        <div id="next" style="display: none;" class="blue w3-button w3-right w3-round w3-large">Next ></div>
    </div>
</div>
<script>
    var nextButton = document.getElementById("next");
    var SELECTED_ELEMENT = undefined;
    var DATA = '''+str(data)+'''
    function selected(elem,select){
        var add = " blue selected ";
        nextButton.style.display = "";
        document.getElementById("guide1").style.display= "none";
        var lst = document.getElementsByClassName("selected");
        for (let i = 0; i < lst.length; i++) {
            var element = lst[i];
            element.className = element.className.replace(add,"");
            element.className = element.className.replace("w4","w3");
        }
        elem.className = elem.className.replace("w3-hover","w4-hover");
        elem.className += add;
        SELECTED_ELEMENT = elem.getAttribute("data-level");
        updateData();
    }
    function updateData(){
        DATA.tier = SELECTED_ELEMENT;
    }
    nextButton.addEventListener("click",()=>{
        if(DATA.tier != undefined){
            var next_url = "'''+next_url+'''".replace("[*data*]",JSON.stringify(DATA));
            window.location.href = next_url;
        }
    });

    setTimeout(()=>{
        if(document.getElementById("guide1").style.display == ""){
            document.getElementById("guide1").style.display= "none";
            return;
        }
        document.getElementById("guide1").style.display= "";
    },10*1000);

    </script>
    '''

def create_vm_step_3(next_url:str,data:dict,group_list = ""):
    return '''
    <div class="w3-container w3-animate-opacity publicSans" >

        
            <div class="w3-display-container" style="height: 80vh;">
                <div class="w3-display-topleft w3-padding-large">
                    <h1 class="bold publicSans">Lastly,</h1>
                </div>
                <div class="w3-display-middle">
                    <p>
                        <b class="w3-padding bolder">Give it a Name</b>
                        <input id="vm_name" type="text" class="w3-border w3-boder-white w3-round-xxlarge grey w3-padding">
                    </p>

                    <div class="w3-container">
                        <div class=" w3-half" style="padding-top: 8px;" >Assign a group</div>
                        <div class="w3-dropdown-hover w3-round-xxlarge w3-half" style="" >
                            <div class="w3-button w3-round-xxlarge grey"><b id="group_box" >Select</b> <i class="fas fa-chevron-down"></i>  </div>
                            <div class="w3-dropdown-content  w3-bar-block ">
                                '''+ str(group_list) +'''
                            </div>
                        </div>
                    </div> 
                </div>
                <div class="w3-display-bottomright w3-padding-large w3-center w3-animate-opacity w3-margin-large" >
                    <div id="next" class="blue w3-button w3-right w3-round w3-large w3-padding-large w3-round-xxlarge"> <i class="fas fa-check "></i> &nbsp; Done ...</div>
                </div>
            </div> 
    </div>
    <script>
        var DATA = '''+str(data)+''';
        document.getElementById("next").addEventListener("click", function() {
            DATA["vm_name"] = document.getElementById("vm_name").value;
            DATA["group"] = document.getElementById("group_box").innerHTML;
            if(DATA.vm_name != undefined && DATA.group != "Select"){
                var next_url = "'''+str(next_url)+'''".replace("[*data*]",JSON.stringify(DATA));
                window.location.href = next_url;
            }
        });
    </script>
    '''
def create_vm_step_4(next_url:str):
    
    
    return '''<h1>VM Creation Started.</h1>
    <script>
        window.location.href = "'''+next_url+'''";
    </script>
    '''