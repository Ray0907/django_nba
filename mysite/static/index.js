let table =$('#datatables').DataTable({
    "processing": true,
    "serverSide": true,
    "ajax": {
        "url": "/api/news",
        "type": "GET"


    },
    "columns": [
        {"data": "title"},
        {"data": "pre_content"},
        {
            "data": 'id',
            "render": function ( data, type, row, meta ) {
                return '<a href="/news/'+data+'">Detail</a>';
               }
        },
        {"data": "post_time"},





    ]
});







