from django.db import models
import PIL
import numpy as np
from cvzone.SelfiSegmentationModule import SelfiSegmentation
from io import BytesIO
import os
from django.core.files.base import ContentFile

# Create your models here.
class Image(models.Model):
    img = models.ImageField(upload_to="BgRemover")
    rmbg_img = models.ImageField(blank=True, upload_to="images_rmbg")

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        pil_img = PIL.Image.open(self.img)
        img = np.array(pil_img)
        segmentor = SelfiSegmentation()
        background_color = (0, 0, 0)
        rmbg = segmentor.removeBG (img, background_color, threshold=0.6)
        buffer = BytesIO()
        output_img = PIL.Image.fromarray(rmbg)
        output_img.save(buffer, format="png")
        val = buffer.getvalue()
        filename = os.path.basename(self.img.name)
        name, _ = filename.split(".")
        self.rmbg_img.save(f"bgrm_{name}.png", ContentFile(val), save = False)
        super().save(*args, **kwargs)

    