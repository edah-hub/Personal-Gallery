function copy(){
  $("#copy_url").select()
  document.execCommand('copy')
  alert('Image link copied to clipboard')
}

function showModal(imgname,imgdesc,imgurl,imgcat,imgloc, imgcity, imgplc,copyurl){
  $("#imageModal").modal("show")
  $(".modal-title").text(imgname)
  $("#imgdescription").text(imgdesc)
  $(".mod-img").attr("src",imgurl)
  $(".imgcat").text('Category: '+imgcat)
  $(".imgloc").text('Country: ' + imgloc)
  $(".imgcity").text('City: ' + imgcity)
  $(".imgplc").text('Place: ' + imgplc)
  $("#copy_url").val(copyurl)
}

// var API_KEY = '27732612-5c33e52ff67af78f897eba61f';
// var URL = "https://pixabay.com/api/?key="+API_KEY+"&q="+encodeURIComponent('red roses');
// $.getJSON(URL, function(data){
// if (parseInt(data.totalHits) > 0)
//     $.each(data.hits, function(i, hit){ console.log(hit.pageURL); });
// else
//     console.log('No hits');
// });


