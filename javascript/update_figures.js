function update_fig_multiwell_dispense() {
  var number = document.getElementById("fig_multiwell_dispense_choice_sheet").value;
  if ((number === "1")){
  var filename = "./figures/multiwell_dispense/multiwell_dispense_3x.mp4";}
  if ((number === "2")){
  var filename = "./figures/multiwell_dispense/multiwell_dispense_1x.mp4";}
  var img = document.getElementById("fig_multiwell_dispense_img");
  img.src = filename;
  var video = img.parentNode;
  video.load();
  video.play();
}

function update_fig_volume_testing() {
  var number = document.getElementById("fig_volume_testing_choice_sheet").value;
  if ((number === "1")){
  var filename = "./figures/volume_testing/zues_SWTT-30-C_PTFE_tube_media_random_volumes.png";}
  if ((number === "2")){
  var filename = "./figures/volume_testing/zues_SWTT-30-C_PTFE_tube_media_fixed_volumes.png";}
  if ((number === "3")){
  var filename = "./figures/volume_testing/zues_SWTT-30-C_PTFE_tube_water_random_volumes.png";}
  if ((number === "4")){
  var filename = "./figures/volume_testing/zues_SWTT-30-C_PTFE_tube_water_fixed_volumes.png";}
  if ((number === "5")){
  var filename = "./figures/volume_testing/idex_1568XL_PEEK_tube_media_random_volumes.png";}
  if ((number === "6")){
  var filename = "./figures/volume_testing/idex_1568XL_PEEK_tube_media_fixed_volumes.png";}
  if ((number === "7")){
  var filename = "./figures/volume_testing/idex_1568XL_PEEK_tube_water_fixed_volumes.png";}  
  var img = document.getElementById("fig_volume_testing_img");
  img.src = filename;
}

function update_fig_image_testing() {
  var number = document.getElementById("fig_image_testing_choice_sheet").value;
  if ((number === "1")){
  var filename = "./figures/image_testing/fl_timelapse_tg.mp4";}
  if ((number === "2")){
  var filename = "./figures/image_testing/fl_timelapse_media.mp4";}
  if ((number === "3")){
  var filename = "./figures/image_testing/dic_timelapse_media_3x.mp4";}
  if ((number === "4")){
  var filename = "./figures/image_testing/fl_tile_media.mp4";}
  if ((number === "5")){
  var filename = "./figures/image_testing/dic_tile_media.mp4";}
  var img = document.getElementById("fig_image_testing_img");
  img.src = filename;
  var video = img.parentNode;
  video.load();
  video.play();
}

function update_fig_bending_ss_tubes() {
  var number = document.getElementById("fig_bending_ss_tubes_choice_sheet").value;
  if ((number === "1")){
  var filename = "./figures/bending_ss_tubes/" + number + ".jpg";}
  if ((number === "2")){
  var filename = "./figures/bending_ss_tubes/" + number + ".jpg";}
  if ((number === "3")){
  var filename = "./figures/bending_ss_tubes/" + number + ".jpg";}
  if ((number === "4")){
  var filename = "./figures/bending_ss_tubes/" + number + ".jpg";}
  if ((number === "5")){
  var filename = "./figures/bending_ss_tubes/" + number + ".jpg";}
  if ((number === "6")){
  var filename = "./figures/bending_ss_tubes/" + number + ".jpg";}
  if ((number === "7")){
  var filename = "./figures/bending_ss_tubes/" + number + ".jpg";}
  if ((number === "8")){
  var filename = "./figures/bending_ss_tubes/" + number + ".jpg";}
  if ((number === "9")){
  var filename = "./figures/bending_ss_tubes/" + number + ".jpg";}
  if ((number === "10")){
  var filename = "./figures/bending_ss_tubes/" + number + ".jpg";}
  if ((number === "11")){
  var filename = "./figures/bending_ss_tubes/" + number + ".jpg";}
  if ((number === "12")){
  var filename = "./figures/bending_ss_tubes/" + number + ".jpg";}
  var img = document.getElementById("fig_bending_ss_tubes_img");
  img.src = filename;
}