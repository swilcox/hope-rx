from django.db import models
from locations.models import Location
from drugs.models import Drug


class Lot(models.Model):
    lot_name = models.CharField(max_length=20,db_index=True)
    drug = models.ForeignKey(Drug)
    expiration_date = models.DateField(null=True,blank=True)
    notes = models.TextField(blank=True,help_text='additional notes about a Lot')

    def __unicode__(self):
        return '%s : %s' % self.lot_name, str(self.drug)


class InventoryQuantity(models.Model):
    location = models.ForeignKey(Location,related_name='inventory')
    lot = models.ForeignKey(Lot,related_name='inventory_counts')
    on_hand = models.IntegerField(default=0)
    on_order = models.IntegerField(default=0)
    in_transit = models.IntegerField(default=0)

    def __unicode__(self):
        return '%s %s on_hand:%s on_order:%s in_transit:%s' % str(self.location), str(self.lot), str(self.on_hand), str(self.on_order), str(self.in_transit)


TRANSFER_STATUS = (('O','Open'),
                   ('T','In-Transit'),
                   ('X','Canceled'),
                   ('R','Received'),
                   ('P','Partially Received'),
                   ('','Unknown'),
)


class Transfer(models.Model):
    origin_location = models.ForeignKey(Location,related_name='originating_transfers',blank=True,null=True)
    destination_location = models.ForeignKey(Location,related_name='incoming_transfers',blank=True,null=True)
    status = models.CharField(max_length=1,choices=TRANSFER_STATUS)
    create_date = models.DateTimeField(null=True,blank=True,auto_created=True)
    ship_date = models.DateTimeField(null=True,blank=True)
    receive_date = models.DateTimeField(null=True,blank=True)

    def __unicode__(self):
        return '%s -> %s (%s)' % str(self.origin_location), str(self.destination_location), self.status


class TransferDetail(models.Model):
    transfer = models.ForeignKey(Transfer,related_name='details')
    lot = models.ForeignKey(Lot,related_name='transfer_details')
    shipped_quantity = models.IntegerField(default=0)
    received_quantity = models.IntegerField(default=0)
    receive_datetime = models.DateTimeField(blank=True,null=True)

    def __unicode__(self):
        return '%s %s' % str(self.transfer), str(self.lot)


class Reason(models.Model):
    description = models.CharField(max_length=30)

    def __unicode__(self):
        return self.description


class Adjustment(models.Model):
    lot = models.ForeignKey(Lot,related_name='adjustments')
    at = models.DateTimeField(auto_created=True)
    quantity = models.IntegerField(default=0)
    reason = models.ForeignKey(Reason)

    def __unicode__(self):
        return '%s %s %s' % str(self.lot), str(self.quantity), str(self.reason)


class Dispense(models.Model):
    lot = models.ForeignKey(Lot,related_name='dispensed')
    at = models.DateTimeField(auto_created=True)
    quantity = models.IntegerField(default=0)
    notes = models.TextField(blank=True)

    def __unicode__(self):
        return '%s %s' % str(self.lot), str(self.quantity)
