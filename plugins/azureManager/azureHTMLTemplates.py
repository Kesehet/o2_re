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
        fetch("https://control.3duverse.com/api/azure_open_api/main?task=get-machine-by-location")

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
            addPoint(19.0760,72.8777,"#1fb2d0",{"cityName":"Mumbai, India","place":"Asia","desc":"Nestled in the heart of Mumbai, our Point of Presence (POP) location is the perfect choice for businesses that demand high-performance cloud services in India. Our Mumbai POP is located in a state-of-the-art data center that offers lightning-fast connectivity and low-latency networking, ensuring that your applications and services run smoothly and efficiently across the Indian subcontinent. With multiple redundant connections and backup power supplies, this POP is designed for maximum uptime and reliability, even during power outages and other unforeseen events. Our expert team of engineers and support staff are on-hand 24/7 to ensure that your cloud services are always running at peak performance, and can provide localized support and expertise for businesses operating in India. Choose our Mumbai POP location for the ultimate in cloud computing performance, reliability, and Indian market expertise."})
            addPoint(28.7041,77.1025,"#1ff2d0",{"cityName":"New Delhi, India","place":"Asia","desc":"Our New Delhi POP is located in the bustling business district of Gurgaon and offers high-speed cloud computing services for businesses in Northern India. With best-in-class connectivity and low latency networking, our state-of-the-art data center ensures maximum uptime and reliability, even during peak traffic periods. Our expert team of engineers and support staff are available 24/7 to provide assistance and support to keep your cloud services running at peak performance. Choose our New Delhi POP for reliable and high-performance cloud computing services in Northern India."});
            addPoint(26.2006,92.9376,"#ffff2d",{"cityName":"Assam, India","place":"Asia","desc":"Our POP location in Assam offers high-speed cloud computing services for businesses operating in the Northeast region of India. Located in a state-of-the-art data center, our Assam POP offers low latency networking and best-in-class connectivity to ensure maximum uptime and reliability for your mission-critical applications and services. With multiple redundant connections and backup power supplies, our POP is designed to keep your cloud services running smoothly, even during unforeseen events. Our expert team of engineers and support staff are available 24/7 to provide assistance and support to keep your cloud services running at peak performance. Choose our Assam POP location for reliable and high-performance cloud computing services in Northeast India."});
            addPoint(13.0827,80.2707,"#ff2dff",{"cityName":"Chennai, India", "place":"Asia" ,"desc":"Welcome to our POP location in Chennai, the bustling metropolis on the Bay of Bengal. Our cloud computing services are second to none, with a state-of-the-art data center located in the heart of the city. With lightning-fast connectivity, cutting-edge hardware, and expert support staff available round-the-clock, you can rest assured that your cloud services are in good hands. Whether you're hosting enterprise applications, building websites, or deploying IoT devices, our Chennai POP offers the perfect blend of reliability, scalability, and performance to meet all of your cloud computing needs."});
            addPoint(55.7558,37.6173,"#0000ff",{"cityName":"Moscow, Russia","place":"Eurasia","desc":"Nestled in the heart of Russia's bustling capital city, our Moscow POP location is the perfect choice for businesses that require high-performance cloud services in the region. Our state-of-the-art data center boasts best-in-class connectivity and low latency networking, ensuring that your mission-critical applications and services operate with maximum uptime and reliability. With a direct connection to the internet exchange point in Moscow, our POP location provides ultra-low latency and a reliable, fast network even during peak traffic periods. Our expert team of engineers and support staff are on-hand 24/7 to provide assistance and support to ensure your cloud services are always running at peak performance. Choose our Moscow POP location for reliable, high-performance cloud computing services that take your business to the next level."
            ,"camera":{
                "position":{    "x": 3.8198439306320013,    "y": 4.3581145087557145,    "z": -1.5542298009582782},
                "rotation":{    "_x": -1.9133644201387254,    "_y": 0.6901341706939985,    "_z": 2.081416391042795,    "_order": "XYZ"}
            }})
            addPoint(89.9831915,-148.6669726,"#FFA500",{"cityName":"DinoPOP (beta)","place":"Pangaea","desc":"Welcome to our POP location in the Dinosaur Age, where we bring cutting-edge cloud computing to the prehistoric world. Our state-of-the-art data center is built from the ground up with the latest in stone and wood technology, and our expert team of pterodactyl engineers and stegosaurus support staff are available 24/7 to provide assistance and support to keep your cloud services running at peak performance. With blazing-fast connectivity provided by our velociraptor network, you can rest assured that your mission-critical applications and services are always up and running. Choose our DinoPOP location for reliable and high-performance cloud computing services in the land before time.",            })
            addPoint(23.0225,72.5714,"#1fb2d0",{"cityName":"Ahmedabad, India","place":"Asia","desc":"Our Point of Presence (POP) in Ahmedabad is located in a state-of-the-art data center that offers high-speed connectivity and low-latency networking across India, ensuring that your cloud services are always available and running smoothly. With multiple redundant connections and backup power supplies, our Ahmedabad POP is designed for maximum uptime and reliability, even during power outages and other unforeseen events. Our expert team of engineers and support staff are on-hand 24/7 to ensure that your cloud services are always running at peak performance, and can provide localized support and expertise for businesses operating in India. Choose our Ahmedabad POP location for reliable and high-performance cloud computing services in Western India."})
            addPoint(11.0168,76.9558,"#1fb2d0",{"cityName":"Coimbatore, India","place":"Asia","desc":"Our Point of Presence (POP) in Coimbatore is the perfect choice for businesses that demand reliable and high-performance cloud services in Southern India. Located in a state-of-the-art data center, our Coimbatore POP offers lightning-fast connectivity and low-latency networking, ensuring that your applications and services run smoothly and efficiently. With multiple redundant connections and backup power supplies, our Coimbatore POP is designed for maximum uptime and reliability, even during power outages and other unforeseen events. Our expert team of engineers and support staff are on-hand 24/7 to ensure that your cloud services are always running at peak performance, and can provide localized support and expertise for businesses operating in Southern India."})

            addPoint(37.7749, -122.4194, "#1fb2d0", {"cityName": "San Francisco, California", "place": "North America", "desc": "Our San Francisco POP is strategically located in the heart of California's tech hub, providing lightning-fast connectivity to businesses that demand high-performance cloud services on the West Coast. The data center offers multiple redundant connections and backup power supplies, ensuring maximum uptime and reliability for our clients. With a team of experienced engineers and support staff available 24/7, we offer localized support and expertise for businesses operating in North America. Choose our San Francisco POP location for the ultimate in cloud computing performance, reliability, and West Coast market expertise."})
            addPoint(40.7128, -74.0060, "#1fb2d0", {"cityName": "New York, New York", "place": "North America", "desc": "Located in the heart of New York City, our POP provides lightning-fast connectivity for businesses that demand high-performance cloud services on the East Coast. Our data center offers multiple redundant connections and backup power supplies, ensuring maximum uptime and reliability for our clients. With a team of experienced engineers and support staff available 24/7, we offer localized support and expertise for businesses operating in North America. Choose our New York POP location for the ultimate in cloud computing performance, reliability, and East Coast market expertise."})
            addPoint(41.8818, -87.6232, "#1fb2d0", {"cityName": "Chicago, Illinois", "place": "North America", "desc": "Our Chicago POP is strategically located in the heart of the Midwest, providing lightning-fast connectivity to businesses that demand high-performance cloud services in the US. The data center offers multiple redundant connections and backup power supplies, ensuring maximum uptime and reliability for our clients. With a team of experienced engineers and support staff available 24/7, we offer localized support and expertise for businesses operating in North America. Choose our Chicago POP location for the ultimate in cloud computing performance, reliability, and Midwest market expertise."})
            addPoint(39.9526, -75.1652, "#1fb2d0", {"cityName": "Philadelphia, Pennsylvania", "place": "North America", "desc": "Our Philadelphia POP is strategically located on the East Coast, providing lightning-fast connectivity to businesses that demand high-performance cloud services in the US. The data center offers multiple redundant connections and backup power supplies, ensuring maximum uptime and reliability for our clients. With a team of experienced engineers and support staff available 24/7, we offer localized support and expertise for businesses operating in North America. Choose our Philadelphia POP location for the ultimate in cloud computing performance, reliability, and East Coast market expertise."})
            addPoint(33.7489, -84.3881, "#1fb2d0", {"cityName": "Atlanta, Georgia", "place": "North America", "desc": "Our Atlanta POP is strategically located in the heart of the South, providing lightning-fast connectivity to businesses that demand high-performance cloud services in the US. The data center offers multiple redundant connections and backup power supplies, ensuring maximum uptime and reliability for our clients. With a team of experienced engineers and support staff available 24/7, we offer localized support and expertise for businesses operating in North America. Choose our Atlanta POP location for the ultimate in cloud computing performance, reliability, and Southern market expertise."})

            addPoint(-33.859972,151.211111,"#1fb2d0",{"cityName":"Sydney, Australia","place":"Oceania","desc":"Our Sydney POP is strategically located in the heart of Australia's financial capital, offering businesses a high-performance cloud computing solution that is optimized for the Australian market. This POP is housed in a state-of-the-art data center, and is designed to deliver lightning-fast connectivity and low-latency networking, ensuring that your applications and services run smoothly and efficiently. With multiple redundant connections and backup power supplies, our Sydney POP is engineered for maximum uptime and reliability, even during power outages and other unforeseen events. Our expert team of engineers and support staff are available 24/7 to ensure that your cloud services are always running at peak performance."})
            addPoint(-37.814,144.96332,"#1fb2d0",{"cityName":"Melbourne, Australia","place":"Oceania","desc":"Our Melbourne POP is located in the heart of Australia's second largest city, providing businesses with a powerful cloud computing solution that is optimized for the local market. This POP is housed in a state-of-the-art data center, and is designed to deliver fast and reliable connectivity, low-latency networking, and maximum uptime and reliability. Our expert team of engineers and support staff are available 24/7 to ensure that your cloud services are always running at peak performance, and can provide localized support and expertise for businesses operating in Australia."})
            addPoint(-31.950527,115.860458,"#1fb2d0",{"cityName":"Perth, Australia","place":"Oceania","desc":"Our Perth POP is strategically located in the heart of Western Australia's largest city, providing businesses with a powerful cloud computing solution that is optimized for the local market. This POP is housed in a state-of-the-art data center, and is designed to deliver fast and reliable connectivity, low-latency networking, and maximum uptime and reliability. Our expert team of engineers and support staff are available 24/7 to ensure that your cloud services are always running at peak performance, and can provide localized support and expertise for businesses operating in Australia."})
            addPoint(-34.9285,138.6007,"#1fb2d0",{"cityName":"Adelaide, Australia","place":"Oceania","desc":"Our Adelaide POP is located in the heart of South Australia's largest city, providing businesses with a powerful cloud computing solution that is optimized for the local market. This POP is housed in a state-of-the-art data center, and is designed to deliver fast and reliable connectivity, low-latency networking, and maximum uptime and reliability. Our expert team of engineers and support staff are available 24/7 to ensure that your cloud services are always running at peak performance, and can provide localized support and expertise for businesses operating in Australia."})
            addPoint(-27.4698,153.0251,"#1fb2d0",{"cityName":"Brisbane, Australia","place":"Oceania","desc":"Our Brisbane POP is strategically located in the heart of Queensland's largest city, providing businesses with a powerful cloud computing solution that is optimized for the local market. This POP is housed in a state-of-the-art data center, and is designed to deliver fast and reliable connectivity, low-latency networking, and maximum uptime and reliability. Our expert team of engineers and support staff are available 24/7 to ensure that your cloud services are always running at peak performance, and can provide localized support and expertise for businesses operating in Australia."})

            // 1. London, United Kingdom
            addPoint(51.5074, -0.1278, "#1fb2d0", {"cityName": "London, United Kingdom", "place": "Europe", "desc": "Our London point of presence (POP) location is situated in the heart of the city, providing high-speed connectivity and low-latency networking for businesses operating in the United Kingdom and beyond. With redundant connections and backup power supplies, our London POP is designed for maximum uptime and reliability, and our expert team of engineers and support staff are on-hand 24/7 to ensure your cloud services run smoothly."});
            // 2. Paris, France
            addPoint(48.8566, 2.3522, "#1fb2d0", {"cityName": "Paris, France", "place": "Europe", "desc": "Our point of presence (POP) in Paris is ideally located to provide high-performance cloud services to businesses across France and the rest of Europe. With lightning-fast connectivity and low-latency networking, our Paris POP is designed to ensure your applications and services run smoothly and efficiently. With multiple redundant connections and backup power supplies, our POP is designed for maximum uptime and reliability, and our team of expert engineers and support staff are on-hand 24/7 to ensure your cloud services are always running at peak performance."});
            // 3. Berlin, Germany
            addPoint(52.5200, 13.4050, "#1fb2d0", {"cityName": "Berlin, Germany", "place": "Europe", "desc": "Our point of presence (POP) in Berlin is perfectly situated to provide high-performance cloud services to businesses across Germany and the rest of Europe. With lightning-fast connectivity and low-latency networking, our Berlin POP is designed to ensure your applications and services run smoothly and efficiently. With multiple redundant connections and backup power supplies, our POP is designed for maximum uptime and reliability, and our team of expert engineers and support staff are on-hand 24/7 to ensure your cloud services are always running at peak performance."});
            // 4. Madrid, Spain
            addPoint(40.4168, -3.7038, "#1fb2d0", {"cityName": "Madrid, Spain", "place": "Europe", "desc": "Our point of presence (POP) location in Madrid is the perfect choice for businesses operating in Spain and across Europe. With high-speed connectivity and low-latency networking, our Madrid POP is designed to ensure your applications and services run smoothly and efficiently. With multiple redundant connections and backup power supplies, our POP is designed for maximum uptime and reliability, and our team of expert engineers and support staff are on-hand 24/7 to ensure your cloud services are always running at peak performance."});
            // 5. Amsterdam, Netherlands
            addPoint(52.3702, 4.8952, "#1fb2d0", {"cityName": "Amsterdam, Netherlands", "place": "Europe", "desc": "Our point of presence (POP) location in Amsterdam is perfectly situated to provide high-performance cloud services to businesses across the Netherlands and the rest of Europe. With lightning-fast connectivity and low-latency networking, our Amsterdam POP is designed to ensure your applications and services run smoothly and efficiently. With multiple redundant connections and backup power supplies, our POP is designed for maximum uptime and reliability, and our team of expert engineers and support staff are on-hand 24/7 to ensure your cloud services are always running at peak performance."});

            addPoint(-33.9249, 18.4241, "#1fb2d0", {"cityName": "Cape Town, South Africa", "place": "Africa", "desc": "Our Cape Town POP is located in one of the most advanced data centers on the African continent, providing lightning-fast connectivity to both local and international businesses. With high-speed internet and redundant power supplies, our Cape Town POP ensures maximum uptime and reliability, even in the face of unforeseen events."});
            addPoint(6.465422, 3.406448, "#1fb2d0", {"cityName": "Lagos, Nigeria", "place": "Africa", "desc": "Our Lagos POP location is the perfect choice for businesses looking for a reliable and high-performance cloud service provider in Africa. Located in a state-of-the-art data center, our POP offers lightning-fast connectivity and low-latency networking, ensuring that your applications and services run smoothly and efficiently across the continent."});
            addPoint(-1.9439, 30.0599, "#1fb2d0", {"cityName": "Kigali, Rwanda", "place": "Africa", "desc": "Our Kigali POP is located in a world-class data center in the heart of Rwanda, providing businesses with access to the latest cloud technologies and ultra-fast connectivity to the African continent. With multiple redundant connections and backup power supplies, our POP ensures maximum uptime and reliability for businesses operating in Africa."});
            addPoint(15.1594, 32.5395, "#1fb2d0", {"cityName": "Khartoum, Sudan", "place": "Africa", "desc": "Our Khartoum POP is the ideal location for businesses looking for a high-performance cloud service provider in Africa. With lightning-fast connectivity and low-latency networking, our POP ensures that your applications and services run smoothly and efficiently across the continent. Our expert team of engineers and support staff are on hand 24/7 to ensure that your cloud services are always running at peak performance."});
            addPoint(9.0578, 7.4951, "#1fb2d0", {"cityName": "Abuja, Nigeria", "place": "Africa", "desc": "Our Abuja POP location provides businesses with access to state-of-the-art cloud technologies and high-performance connectivity to the African continent. Located in a world-class data center, our POP ensures maximum uptime and reliability, even in the face of unforeseen events. Choose our Abuja POP for the ultimate in cloud computing performance and reliability in Africa."})

            addPoint(25.2048, 55.2708, "#1fb2d0", {"cityName": "Dubai, United Arab Emirates", "place": "Middle East", "desc": "Our POP location in Dubai is strategically located to provide the highest level of cloud computing services to businesses across the Middle East. Situated in one of the most advanced data centers in the region, our POP offers the latest technology, high-speed connectivity, and top-notch security for maximum uptime and reliability."})
            addPoint(25.7617, -80.1918, "#1fb2d0", {"cityName": "Miami, Florida, USA", "place": "North America", "desc": "Our POP location in Miami offers businesses in the region access to high-performance cloud computing services for their applications and services. Our data center offers lightning-fast connectivity and low-latency networking, ensuring smooth and efficient operations."})
            addPoint(26.8206, 30.8025, "#1fb2d0", {"cityName": "Luxor, Egypt", "place": "Africa", "desc": "Located in the historic city of Luxor, our POP location offers businesses access to cloud computing services in the heart of Africa. With lightning-fast connectivity and top-notch security, our data center ensures maximum uptime and reliability for your applications and services."})
            addPoint(33.5731, -7.5898, "#1fb2d0", {"cityName": "Casablanca, Morocco", "place": "Africa", "desc": "Our POP location in Casablanca offers businesses in the region access to high-performance cloud computing services. Our data center offers lightning-fast connectivity and top-notch security, ensuring maximum uptime and reliability for your applications and services."})
            addPoint(31.5096, 34.4660, "#1fb2d0", {"cityName": "Ashdod, Israel", "place": "Middle East", "desc": "Our POP location in Ashdod offers businesses in the region access to high-performance cloud computing services. Our data center offers lightning-fast connectivity and top-notch security, ensuring maximum uptime and reliability for your applications and services."})
            addPoint(12.8628, 30.2176, "#1fb2d0", {"cityName": "Wau, South Sudan", "place": "Africa", "desc": "Our POP location in Wau offers businesses access to cloud computing services in the heart of Africa. With lightning-fast connectivity and top-notch security, our data center ensures maximum uptime and reliability for your applications and services."})
            addPoint(37.9358, 27.3325, "#1fb2d0", {"cityName": "Izmir, Turkey", "place": "Middle East", "desc": "Our POP location in Izmir offers businesses in the region access to high-performance cloud computing services. Our data center offers lightning-fast connectivity and top-notch security, ensuring maximum uptime and reliability for your applications and services."})
            addPoint(31.7917, -7.0926, "#1fb2d0", {"cityName": "Marrakesh, Morocco", "place": "Africa", "desc": "Our POP location in Marrakesh offers businesses in the region access to high-performance cloud computing services. Our data center offers lightning-fast connectivity and top-notch security, ensuring maximum uptime and reliability for your applications and services."})

            addPoint(-34.6037,-58.3816,"#1fb2d0",{"cityName":"Buenos Aires, Argentina","place":"South America","desc":"Our Buenos Aires Point of Presence (POP) location is strategically located in Argentina's bustling capital city. This state-of-the-art data center offers lightning-fast connectivity and low-latency networking, making it the perfect choice for businesses that demand high-performance cloud services in the region. With multiple redundant connections and backup power supplies, this POP is designed for maximum uptime and reliability. Our expert team of engineers and support staff are on-hand 24/7 to ensure that your cloud services are always running at peak performance."})
            addPoint(-23.5505,-46.6333,"#1fb2d0",{"cityName":"São Paulo, Brazil","place":"South America","desc":"Nestled in the heart of São Paulo, our Point of Presence (POP) location is the perfect choice for businesses that demand high-performance cloud services in Brazil. Our São Paulo POP is located in a state-of-the-art data center that offers lightning-fast connectivity and low-latency networking, ensuring that your applications and services run smoothly and efficiently across the country. With multiple redundant connections and backup power supplies, this POP is designed for maximum uptime and reliability, even during power outages and other unforeseen events. Our expert team of engineers and support staff are on-hand 24/7 to ensure that your cloud services are always running at peak performance."})
            addPoint(-22.9068,-43.1729,"#1fb2d0",{"cityName":"Rio de Janeiro, Brazil","place":"South America","desc":"Our Rio de Janeiro Point of Presence (POP) location is strategically located in Brazil's second-largest city. This state-of-the-art data center offers lightning-fast connectivity and low-latency networking, making it the perfect choice for businesses that demand high-performance cloud services in the region. With multiple redundant connections and backup power supplies, this POP is designed for maximum uptime and reliability. Our expert team of engineers and support staff are on-hand 24/7 to ensure that your cloud services are always running at peak performance."})
            addPoint(-30.0277,-51.2287,"#1fb2d0",{"cityName":"Porto Alegre, Brazil","place":"South America","desc":"Our Porto Alegre Point of Presence (POP) location is strategically located in southern Brazil. This state-of-the-art data center offers lightning-fast connectivity and low-latency networking, making it the perfect choice for businesses that demand high-performance cloud services in the region. With multiple redundant connections and backup power supplies, this POP is designed for maximum uptime and reliability. Our expert team of engineers and support staff are on-hand 24/7 to ensure that your cloud services are always running at peak performance."})
            addPoint(-34.9011,-56.1645,"#1fb2d0",{"cityName":"Montevideo, Uruguay","place":"South America","desc":"Our Montevideo Point of Presence (POP) location is strategically located in Uruguay's capital city. This state-of-the-art data center offers lightning-fast connectivity and low-latency networking, making it the perfect choice for businesses that demand high-performance cloud services in the region. With multiple redundant connections and backup power supplies, this POP is designed for maximum uptime and reliability. Our expert team of engineers and support staff are on-hand 24/7 to ensure that your cloud services are always running at peak performance."})

            addPoint(-12.0464,-77.0428,"#1fb2d0",{"cityName":"Lima, Peru","place":"South America","desc":"Located in the heart of Lima, our Point of Presence (POP) provides high-performance cloud services across the South American region. Our Lima POP is located in a state-of-the-art data center, offering lightning-fast connectivity and low-latency networking to ensure that your applications and services run smoothly and efficiently. With multiple redundant connections and backup power supplies, this POP is designed for maximum uptime and reliability, even during power outages and other unforeseen events. Our expert team of engineers and support staff are available 24/7 to ensure that your cloud services are always running at peak performance."})
            addPoint(-33.4489,-70.6693,"#1fb2d0",{"cityName":"Santiago, Chile","place":"South America","desc":"Our Santiago POP is the perfect choice for businesses that demand high-performance cloud services in Chile and the surrounding region. Our POP is located in a state-of-the-art data center, offering lightning-fast connectivity and low-latency networking to ensure that your applications and services run smoothly and efficiently. With multiple redundant connections and backup power supplies, this POP is designed for maximum uptime and reliability, even during power outages and other unforeseen events. Our expert team of engineers and support staff are available 24/7 to ensure that your cloud services are always running at peak performance."})
            addPoint(10.4806,-66.9036,"#1fb2d0",{"cityName":"Caracas, Venezuela","place":"South America","desc":"Our Caracas POP location offers a strategic gateway to the Venezuelan market and wider South America. This state-of-the-art data center is located in a prime location in Caracas, providing high-speed connectivity and low-latency networking to the region. With multiple redundant connections and backup power supplies, our POP is designed for maximum uptime and reliability, even during power outages and other unforeseen events. Our team of experts provides 24/7 support to ensure that your cloud services are always running at peak performance, and can provide localized support and expertise for businesses operating in Venezuela."})
            addPoint(-36.8485,174.7633,"#1fb2d0",{"cityName":"Auckland, New Zealand","place":"Oceania","desc":"Located in the bustling city of Auckland, our Point of Presence (POP) is designed to deliver high-performance cloud computing services to businesses across New Zealand and the Asia-Pacific region. Our Auckland POP is housed in a modern data center facility, with advanced security features, redundant power supplies, and lightning-fast connectivity to ensure maximum uptime and performance. Our expert team of engineers and support staff are on-hand 24/7 to ensure that your cloud services are always running at peak performance, and can provide localized support and expertise for businesses operating in New Zealand. Choose our Auckland POP location for fast, reliable, and secure cloud computing services."})
            addPoint(-21.0635,-149.4653,"#1fb2d0",{"cityName":"Honolulu, Hawaii","place":"North America","desc":"Our Point of Presence (POP) location in Honolulu, Hawaii is the perfect choice for businesses that demand high-performance cloud services in the Pacific Rim. Located in a state-of-the-art data center facility, our Honolulu POP offers lightning-fast connectivity and low-latency networking, ensuring that your applications and services run smoothly and efficiently across the Pacific region. With multiple redundant connections and backup power supplies, this POP is designed for maximum uptime and reliability, even during power outages and other unforeseen events. Our expert team of engineers and support staff are on-hand 24/7 to ensure that your cloud services are always running at peak performance, and can provide localized support and expertise for businesses operating in Hawaii and the Pacific region."})

            addPoint(51.1282,71.4304,"#1fb2d0",{"cityName":"Astana, Kazakhstan","place":"Asia","desc":"Our POP location in Astana, the capital city of Kazakhstan, offers a high-performance cloud infrastructure with lightning-fast connectivity, low latency networking, and maximum uptime and reliability. Located in a state-of-the-art data center, our POP is designed to meet the needs of businesses operating in Central Asia and beyond."})
            addPoint(34.5553,69.2075,"#1fb2d0",{"cityName":"Kabul, Afghanistan","place":"Asia","desc":"Our Kabul POP location offers a secure, high-performance cloud infrastructure that is designed to meet the needs of businesses operating in Afghanistan and beyond. With lightning-fast connectivity, low latency networking, and multiple redundant connections and backup power supplies, our POP ensures maximum uptime and reliability for your cloud services."})
            addPoint(47.8864,106.9057,"#1fb2d0",{"cityName":"Ulaanbaatar, Mongolia","place":"Asia","desc":"Located in the heart of Ulaanbaatar, our POP location in Mongolia provides high-performance cloud services with lightning-fast connectivity, low latency networking, and maximum uptime and reliability. Our expert team of engineers and support staff are on-hand 24/7 to ensure that your cloud services are always running at peak performance, and can provide localized support and expertise for businesses operating in Mongolia and the surrounding region."})
            addPoint(39.9042,116.4074,"#1fb2d0",{"cityName":"Beijing, China","place":"Asia","desc":"Our Beijing POP location offers a secure, high-performance cloud infrastructure that is designed to meet the needs of businesses operating in China and beyond. With lightning-fast connectivity, low latency networking, and multiple redundant connections and backup power supplies, our POP ensures maximum uptime and reliability for your cloud services. Our expert team of engineers and support staff are on-hand 24/7 to ensure that your cloud services are always running at peak performance, and can provide localized support and expertise for businesses operating in China."})

            setOptimalList();
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

def create_vm_step_3(next_url:str,data:dict):
    return '''
    <div class="w3-container w3-animate-opacity publicSans" >
    
        
            <div class="w3-display-container" style="height: 80vh;">
                <div class="w3-display-topleft w3-padding-large">
                    <h1 class="bold publicSans">Lastly,</h1>
                </div>
                <div class="w3-display-middle">
                    <p>
                        <b class="w3-padding bolder">Give it a Name</b>
                        <input type="text" class="w3-border w3-boder-white w3-round-xxlarge grey w3-padding">
                    </p>

                    <div class="w3-container">
                        <div class=" w3-half" style="padding-top: 8px;" >Assign a group</div>
                        <div class="w3-dropdown-hover w3-round-xxlarge w3-half" style="" >
                            <div class="w3-button w3-round-xxlarge grey">Groups <i class="fas fa-chevron-down"></i>  </div>
                            <div class="w3-dropdown-content  w3-bar-block ">
                                <a href="#" class="w3-bar-item w3-button w3-round-xxlarge grey">Link 1</a>
                                <a href="#" class="w3-bar-item w3-button w3-round-xxlarge grey">Link 2</a>
                                <a href="#" class="w3-bar-item w3-button w3-round-xxlarge grey">Link 3</a>
                            </div>
                        </div>
                    </div> 
                </div>
                <div class="w3-display-bottomright w3-padding-large w3-center w3-animate-opacity w3-margin-large" >
                    <div id="next" class="blue w3-button w3-right w3-round w3-large w3-padding-large w3-round-xxlarge"> <i class="fas fa-check "></i> &nbsp; Done ...</div>
                </div>
            </div> 
    </div>
    '''