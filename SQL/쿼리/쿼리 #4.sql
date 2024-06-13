ALTER TABLE beatmaps AUTO_INCREMENT=0; 
SET @COUNT = 0; 
UPDATE beatmaps SET beatmaps.id = @COUNT:=@COUNT+1;