#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HealthDrugCatalogueItem(object):

    def __init__(self):
        self._catalogue_listed = None
        self._dosage_forms = None
        self._drug_classification = None
        self._general_name = None
        self._inventory = None
        self._item_id = None
        self._item_name = None
        self._manufacturer_name = None
        self._max_purchase_quantity = None
        self._min_purchase_quantity = None
        self._national_medicine_permission_no = None
        self._price = None
        self._specifications = None
        self._support_emergency_delivery = None
        self._usage_dosage = None

    @property
    def catalogue_listed(self):
        return self._catalogue_listed

    @catalogue_listed.setter
    def catalogue_listed(self, value):
        self._catalogue_listed = value
    @property
    def dosage_forms(self):
        return self._dosage_forms

    @dosage_forms.setter
    def dosage_forms(self, value):
        self._dosage_forms = value
    @property
    def drug_classification(self):
        return self._drug_classification

    @drug_classification.setter
    def drug_classification(self, value):
        self._drug_classification = value
    @property
    def general_name(self):
        return self._general_name

    @general_name.setter
    def general_name(self, value):
        self._general_name = value
    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        self._inventory = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def manufacturer_name(self):
        return self._manufacturer_name

    @manufacturer_name.setter
    def manufacturer_name(self, value):
        self._manufacturer_name = value
    @property
    def max_purchase_quantity(self):
        return self._max_purchase_quantity

    @max_purchase_quantity.setter
    def max_purchase_quantity(self, value):
        self._max_purchase_quantity = value
    @property
    def min_purchase_quantity(self):
        return self._min_purchase_quantity

    @min_purchase_quantity.setter
    def min_purchase_quantity(self, value):
        self._min_purchase_quantity = value
    @property
    def national_medicine_permission_no(self):
        return self._national_medicine_permission_no

    @national_medicine_permission_no.setter
    def national_medicine_permission_no(self, value):
        self._national_medicine_permission_no = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def specifications(self):
        return self._specifications

    @specifications.setter
    def specifications(self, value):
        self._specifications = value
    @property
    def support_emergency_delivery(self):
        return self._support_emergency_delivery

    @support_emergency_delivery.setter
    def support_emergency_delivery(self, value):
        self._support_emergency_delivery = value
    @property
    def usage_dosage(self):
        return self._usage_dosage

    @usage_dosage.setter
    def usage_dosage(self, value):
        self._usage_dosage = value


    def to_alipay_dict(self):
        params = dict()
        if self.catalogue_listed:
            if hasattr(self.catalogue_listed, 'to_alipay_dict'):
                params['catalogue_listed'] = self.catalogue_listed.to_alipay_dict()
            else:
                params['catalogue_listed'] = self.catalogue_listed
        if self.dosage_forms:
            if hasattr(self.dosage_forms, 'to_alipay_dict'):
                params['dosage_forms'] = self.dosage_forms.to_alipay_dict()
            else:
                params['dosage_forms'] = self.dosage_forms
        if self.drug_classification:
            if hasattr(self.drug_classification, 'to_alipay_dict'):
                params['drug_classification'] = self.drug_classification.to_alipay_dict()
            else:
                params['drug_classification'] = self.drug_classification
        if self.general_name:
            if hasattr(self.general_name, 'to_alipay_dict'):
                params['general_name'] = self.general_name.to_alipay_dict()
            else:
                params['general_name'] = self.general_name
        if self.inventory:
            if hasattr(self.inventory, 'to_alipay_dict'):
                params['inventory'] = self.inventory.to_alipay_dict()
            else:
                params['inventory'] = self.inventory
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.manufacturer_name:
            if hasattr(self.manufacturer_name, 'to_alipay_dict'):
                params['manufacturer_name'] = self.manufacturer_name.to_alipay_dict()
            else:
                params['manufacturer_name'] = self.manufacturer_name
        if self.max_purchase_quantity:
            if hasattr(self.max_purchase_quantity, 'to_alipay_dict'):
                params['max_purchase_quantity'] = self.max_purchase_quantity.to_alipay_dict()
            else:
                params['max_purchase_quantity'] = self.max_purchase_quantity
        if self.min_purchase_quantity:
            if hasattr(self.min_purchase_quantity, 'to_alipay_dict'):
                params['min_purchase_quantity'] = self.min_purchase_quantity.to_alipay_dict()
            else:
                params['min_purchase_quantity'] = self.min_purchase_quantity
        if self.national_medicine_permission_no:
            if hasattr(self.national_medicine_permission_no, 'to_alipay_dict'):
                params['national_medicine_permission_no'] = self.national_medicine_permission_no.to_alipay_dict()
            else:
                params['national_medicine_permission_no'] = self.national_medicine_permission_no
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.specifications:
            if hasattr(self.specifications, 'to_alipay_dict'):
                params['specifications'] = self.specifications.to_alipay_dict()
            else:
                params['specifications'] = self.specifications
        if self.support_emergency_delivery:
            if hasattr(self.support_emergency_delivery, 'to_alipay_dict'):
                params['support_emergency_delivery'] = self.support_emergency_delivery.to_alipay_dict()
            else:
                params['support_emergency_delivery'] = self.support_emergency_delivery
        if self.usage_dosage:
            if hasattr(self.usage_dosage, 'to_alipay_dict'):
                params['usage_dosage'] = self.usage_dosage.to_alipay_dict()
            else:
                params['usage_dosage'] = self.usage_dosage
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HealthDrugCatalogueItem()
        if 'catalogue_listed' in d:
            o.catalogue_listed = d['catalogue_listed']
        if 'dosage_forms' in d:
            o.dosage_forms = d['dosage_forms']
        if 'drug_classification' in d:
            o.drug_classification = d['drug_classification']
        if 'general_name' in d:
            o.general_name = d['general_name']
        if 'inventory' in d:
            o.inventory = d['inventory']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'manufacturer_name' in d:
            o.manufacturer_name = d['manufacturer_name']
        if 'max_purchase_quantity' in d:
            o.max_purchase_quantity = d['max_purchase_quantity']
        if 'min_purchase_quantity' in d:
            o.min_purchase_quantity = d['min_purchase_quantity']
        if 'national_medicine_permission_no' in d:
            o.national_medicine_permission_no = d['national_medicine_permission_no']
        if 'price' in d:
            o.price = d['price']
        if 'specifications' in d:
            o.specifications = d['specifications']
        if 'support_emergency_delivery' in d:
            o.support_emergency_delivery = d['support_emergency_delivery']
        if 'usage_dosage' in d:
            o.usage_dosage = d['usage_dosage']
        return o


