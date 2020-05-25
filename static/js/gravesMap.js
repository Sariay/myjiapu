( function () {

    //初始化地图对象
    let gravesMap = new T.Map('gravesMap',  {datasourcesControl: true});
    const map = {
        centerXy: new T.LngLat(105.1087822401263, 26.951609166825268),
        zoomLevel: 14,
        circleRadius: 3000,
        circleStyle: {color:"blue",weight:5,opacity:0.5,fillColor:"#FFFFFF",fillOpacity:0.1,lineStyle:"solid"}
    }
    // let map = new T.Map('gravesMap',  {datasourcesControl: true});
    // let xy = new T.LngLat(105.1087822401263, 26.951609166825268);
    // let zoom = 14;

    gravesMap.centerAndZoom(map.centerXy, map.zoomLevel);

    //地图上添加图层：圆
    // let style = {color:"blue",weight:5,opacity:0.5,fillColor:"#FFFFFF",fillOpacity:0.1,lineStyle:"solid"};
    gravesMap.addOverLay(new T.Circle(map.centerXy, map.circleRadius, map.circleStyle));

    //地图上添加控件
    gravesMap.addControl(new T.Control.MapType());
    gravesMap.addControl(new T.Control.Zoom());
    gravesMap.addControl(new T.Control.Scale());
            
    let gravesInfo = [
        ["李龙生墓址，大祖考。",105.11579504109773, 26.948047023516608],
        
        ["罗正英墓址，曾祖妣。",105.11592226504409, 26.948575777384125],
        
        ["李世合墓址，曾祖考。",105.11581215491195, 26.948515776460507],	
                
        ["李强墓址，幺叔考。",105.11572487545993, 26.948411600727383],	
                
        ["陈二姐墓址，大祖妣，夫李少安。",105.11443674106862, 26.946046247387727],	
        
        ["李万顺墓址，二曾祖考。",105.1143597331299, 26.94703176203735],
        
        ["李少安墓址，大祖考。",105.11394393194132, 26.94756803183461],	
        
        ["待考墓址：二老祖婆,名王讷讷,夫李万顺。",105.11344573233136, 26.945802027665483],
        
        ["赵明英墓址，祖妣，夫李光荣。",105.11595022894986, 26.947451457163638],
        
        ["待考：田坝寨支系坟茔。",105.11611102086107, 26.947381882666367],
        
        ["李小银墓址，大曾祖考。",105.12026957902843, 26.950496658591913],
        
        ["李政墓址，大伯考。",105.12171381483068, 26.954715698249313],	
            
        ["失考墓址。",105.11802557567074, 26.950879317681387],		
        
        ["待考:支系始祖1，墓自大干河迁移至此。长房支系。",105.11810070777683, 26.95021937903507],
        
        ["待考:支系始祖2，墓自大干河迁移至此。长房支系。",105.1181454069633, 26.95023737498499],
        
        ["始迁祖墓址，萨拉suka等。",105.11911608299182, 26.94938937836576],
        
        ["待考:疑似李五大爷。",105.11937384572204, 26.94970782654998],
        
        ["失考墓址。",105.11962413951048, 26.949660891019757],
        
        ["失考墓址。",105.11969923377514, 26.949743883864834],
        
        ["失考墓址。",105.1197661665651, 2694980069971647],
        
        ["失考墓址。",105.11979718056357, 26.949902497833182],
        
        ["李德音墓址，三曾祖考。",105.10849629455679, 26.958470842270128],
        
        ["李光辉墓址，幺祖考。",105.10088772411653, 26.955871090139343],
        
        ["李光荣墓址，祖考。",105.09415152742874, 26.95537637811977],
        
        ["待考墓址，织金支系:祖考。",105.1087822401263, 26.951609166825268],
        
        ["三老祖婆墓址，曾祖妣，夫李德音。",105.11773750588264, 26.948514194753766],
        
        ["失考墓址。",105.11769975646477, 26.95060212834504],
        
        ["老天天墓址1。",105.11642302150112, 26.94787178267451],
        
        ["老天天墓址2。",105.1164161661278, 26.947840444107243],
        
        ["罗永凤墓址，幺祖妣，夫李光辉。",105.11738607600549, 26.94843643595013],
    ];

    const openInfo = function(markerText,e){
        let point = e.lnglat,
            marker = new T.Marker(point), // 创建标注
            markerInfoWin = new T.InfoWindow(markerText,{offset:new T.Point(0,-30)}); // 创建信息窗口对象
        
            gravesMap.openInfoWindow(markerInfoWin,point); //开启信息窗口
    }

    const addClickHandler = function(markerText,marker){

        marker.addEventListener("click",function(e){
            openInfo(markerText,e)}
        );

    }

    for( let i=0; i<gravesInfo.length; i++ ){
        // 创建标注
        let marker = new T.Marker(new T.LngLat(gravesInfo[i][1],gravesInfo[i][2])),  
            markerText = gravesInfo[i][0];

        // 将标注添加到地图中
        gravesMap.addOverLay(marker); 

        addClickHandler(markerText,marker);
    }  
})();