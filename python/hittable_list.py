from hittable import Hit, Hittable

class HittableList:
    def __init__(self):
        self.objects = []

    def clear(self):
        self.objects = []

    def add(self, obj):
        self.objects.append(obj)

    def hit(self, r, ray_tmin, ray_tmax, rec):
        temp_hit = Hit()
        has_hit = False
        closest = ray_tmax
        
        for obj in self.objects:
            if obj.hit(r, ray_tmin, closest, rec):
                has_hit = True
                closest, rec.t, rec.p, rec.normal = temp_hit.t, temp_hit.t, temp_hit.p, temp_hit.normal

        return has_hit