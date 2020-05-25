(function(){

    let lineageTree = echarts.init(document.getElementById('lineageTree'));
    let data = {
        "name": "李走则",
        "value": 11,
        "children": [
            {
                "name": "李云合",
                "value": 21,
                "children": [
                    {
                        "name": "李雪清",
                        "value": 31,
                        "children": [
                            {"name": "李小银", "value": 41},
                            {
                                "name": "李万顺", 
                                "value": 42,
                                "children": [
                                    {"name": "佚名（女）"},
                                    {"name": "李贵英（女）"},
                                ]
                            },
                            {
                                "name": "李德音", 
                                "value": 43,
                                "children": [
                                    {"name": "李龙生", "value": 51},
                                ]									
                            },
                            {
                                "name": "李世合",
                                "value": 44,
                                "children": [
                                    {
                                        "name": "李少安", "value": 52,
                                        "children": [
                                            {"name": "佚名（女）"},
                                            {"name": "佚名（女）"},
                                            {"name": "佚名（女）"},
                                            {"name": "佚名，待考"},
                                        ]									 		
                                    },
                                    {
                                        "name": "李光荣",
                                        "value": 53,
                                        "children": [
                                            {
                                                "name": "李政", 
                                                value: 61,
                                                "children": [
                                                    {"name": "李阳（女）"},
                                                    {"name": "李向阳（女）"},
                                                ]
                                            },
                                            {
                                                "name": "李明", 
                                                "value": 62,
                                                "children": [
                                                    {"name": "李驰骋","value": 71,},
                                                    {"name": "李驰航","value": 72,},
                                                    {"name": "李倩（女）"},
                                                ]
                                            },
                                            {
                                                "name": "李强", 
                                                "value": 63,
                                                "children": [
                                                    {"name": "李春江", "value": 73,},
                                                    {"name": "李珊瑚", "value": 74,},
                                                    {"name": "李迤佳（女）"},
                                                    {"name": "李雨柔（女）"},
                                                ]
                                            },
                                            {"name": "李敏（女）"},
                                            {"name": "李艳（女）"},
                                            {"name": "李芳（女）"},
                                            {
                                                "name": "李训海", 
                                                "value": 64,
                                                "children": [
                                                    {"name": "李远鸿", "value": 75,},
                                                    {"name": "李远玺", "value": 76,},
                                                    {"name": "李艳群（女）"},
                                                ]
                                            },
                                        ]	
                                    },
                                    {
                                        "name": "李光辉",
                                        "value": 54,
                                        "children": [
                                            {"name": "李正忠", "value": 65,},
                                            {
                                                "name": "李义", 
                                                "value": 66,
                                                "children": [
                                                    {"name": "李兴", "value": 77,},
                                                ]
                                            },
                                            {"name": "李柯美（女）"},
                                        ]	
                                    },
                                ]									
                            },
                            {"name": "佚名（女）"},
                            {"name": "佚名（女）"},
                            {"name": "李春姐（女）"},
                        ]
                    },
                    {
                        "name": "李京华",
                        "value": 32,
                        "children": [
                            {
                                "name": "李洪顺",
                                "value": 45,
                                "children": [
                                    {
                                        "name": "李少明", 
                                        "value": 55,
                                        "children": [
                                            {"name": "李开桥", "value": 67,},
                                            {
                                                "name": "李明友", 
                                                "value": 68,
                                                "children": [
                                                    {"name": "李建", "value": 78,},
                                                    {"name": "李进", "value": 79,},
                                                    {"name": "李甜（女）"},
                                                    {"name": "李丽甜（女）"},						
                                                ]
                                            },
                                            {
                                                "name": "李开华",
                                                "value": 69,
                                                "children": [
                                                    {"name": "李菊（女）"},						
                                                ]
                                            },
                                            {"name": "李开珍（女）"},
                                            {"name": "李开秀（女）"},
                                            {"name": "李开琴（女）"},
                                            {"name": "李开敏（女）"},
                                        ]
                                    }
                                ]									 
                            },
                            {"name": "李洪安", "value": 46},
                            {"name": "佚名", "value": 47},
                        ]
                    }
                ]
            },
            ] 
    };
    
    let option = {
        // backgroundColor: '#eef1f6',
        backgroundColor: '#ffffff',
        color: '#000000',
        title: {
            show: true,
            text: '长房世系图',
            textAlign: 'auto',
            textVerticalAlign: 'auto',
            top: 10,
            left: 'center',		
        },
        tooltip: {
            trigger: 'item',
            triggerOn: 'mousemove'
        },
        toolbox: {
            show: true,
            orient: 'vertical',
            feature: {
                dataView: {readOnly: false},
                restore: {show: true},
                saveAsImage: {type: 'png'}
            }
        },
        series:[
            {
                type: 'tree',
                id: 0,
                name: 'family-true',
                data: [data],
    
                top: '5%',
                bottom: '5%',
                left: '10%',
                right: '10%',
                
                layout: 'orthogonal',
                orient: 'LR',
                
                // symbol: 'circle',
                symbolSize: 10,
                
                edgeShape: 'polyline',
                edgeForkPosition: '50%',
                roam: true,

                expandAndCollapse: true,
                initialTreeDepth: -1,
                
                lineStyle: {
                    width: 2
                },
    
                label: {
                    show: true,
                    backgroundColor: '#ffffff',
                    color: '#000000',
                    position: 'left',
                    verticalAlign: 'middle',
                    align: 'right',
                    fontFamily: 'sans-serif',
                    lineHeight: 12,
                    fontSize: 14,
                    borderRadius: 2,
                    padding: 5	
                },
    
                leaves: {
                    label: {
                        position: 'right',
                        verticalAlign: 'middle',
                        align: 'left'
                    }
                },
    
                animationDuration: 550,
                animationDurationUpdate: 750,
                animationEasing: 'quinticln'
            }
        ]
    };
    
    lineageTree.setOption(option);
    lineageTree.resize();

})();