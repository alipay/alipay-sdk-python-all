#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbadvertVoucherManual import KbadvertVoucherManual


class KbAdvertSubjectVoucherResponse(object):

    def __init__(self):
        self._brand_name = None
        self._city_ids = None
        self._cover = None
        self._daily_inventory = None
        self._gmt_end = None
        self._gmt_start = None
        self._logo = None
        self._manuals = None
        self._merchant_name = None
        self._partner_id = None
        self._purchase_mode = None
        self._shop_ids = None
        self._threshold_amount = None
        self._total_inventory = None
        self._voucher_id = None
        self._voucher_name = None
        self._voucher_org_value = None
        self._voucher_type = None
        self._voucher_value = None

    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def city_ids(self):
        return self._city_ids

    @city_ids.setter
    def city_ids(self, value):
        if isinstance(value, list):
            self._city_ids = list()
            for i in value:
                self._city_ids.append(i)
    @property
    def cover(self):
        return self._cover

    @cover.setter
    def cover(self, value):
        self._cover = value
    @property
    def daily_inventory(self):
        return self._daily_inventory

    @daily_inventory.setter
    def daily_inventory(self, value):
        self._daily_inventory = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_start(self):
        return self._gmt_start

    @gmt_start.setter
    def gmt_start(self, value):
        self._gmt_start = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def manuals(self):
        return self._manuals

    @manuals.setter
    def manuals(self, value):
        if isinstance(value, list):
            self._manuals = list()
            for i in value:
                if isinstance(i, KbadvertVoucherManual):
                    self._manuals.append(i)
                else:
                    self._manuals.append(KbadvertVoucherManual.from_alipay_dict(i))
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def purchase_mode(self):
        return self._purchase_mode

    @purchase_mode.setter
    def purchase_mode(self, value):
        self._purchase_mode = value
    @property
    def shop_ids(self):
        return self._shop_ids

    @shop_ids.setter
    def shop_ids(self, value):
        if isinstance(value, list):
            self._shop_ids = list()
            for i in value:
                self._shop_ids.append(i)
    @property
    def threshold_amount(self):
        return self._threshold_amount

    @threshold_amount.setter
    def threshold_amount(self, value):
        self._threshold_amount = value
    @property
    def total_inventory(self):
        return self._total_inventory

    @total_inventory.setter
    def total_inventory(self, value):
        self._total_inventory = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value
    @property
    def voucher_name(self):
        return self._voucher_name

    @voucher_name.setter
    def voucher_name(self, value):
        self._voucher_name = value
    @property
    def voucher_org_value(self):
        return self._voucher_org_value

    @voucher_org_value.setter
    def voucher_org_value(self, value):
        self._voucher_org_value = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value
    @property
    def voucher_value(self):
        return self._voucher_value

    @voucher_value.setter
    def voucher_value(self, value):
        self._voucher_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.city_ids:
            if isinstance(self.city_ids, list):
                for i in range(0, len(self.city_ids)):
                    element = self.city_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.city_ids[i] = element.to_alipay_dict()
            if hasattr(self.city_ids, 'to_alipay_dict'):
                params['city_ids'] = self.city_ids.to_alipay_dict()
            else:
                params['city_ids'] = self.city_ids
        if self.cover:
            if hasattr(self.cover, 'to_alipay_dict'):
                params['cover'] = self.cover.to_alipay_dict()
            else:
                params['cover'] = self.cover
        if self.daily_inventory:
            if hasattr(self.daily_inventory, 'to_alipay_dict'):
                params['daily_inventory'] = self.daily_inventory.to_alipay_dict()
            else:
                params['daily_inventory'] = self.daily_inventory
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.gmt_start:
            if hasattr(self.gmt_start, 'to_alipay_dict'):
                params['gmt_start'] = self.gmt_start.to_alipay_dict()
            else:
                params['gmt_start'] = self.gmt_start
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.manuals:
            if isinstance(self.manuals, list):
                for i in range(0, len(self.manuals)):
                    element = self.manuals[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.manuals[i] = element.to_alipay_dict()
            if hasattr(self.manuals, 'to_alipay_dict'):
                params['manuals'] = self.manuals.to_alipay_dict()
            else:
                params['manuals'] = self.manuals
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.purchase_mode:
            if hasattr(self.purchase_mode, 'to_alipay_dict'):
                params['purchase_mode'] = self.purchase_mode.to_alipay_dict()
            else:
                params['purchase_mode'] = self.purchase_mode
        if self.shop_ids:
            if isinstance(self.shop_ids, list):
                for i in range(0, len(self.shop_ids)):
                    element = self.shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.shop_ids, 'to_alipay_dict'):
                params['shop_ids'] = self.shop_ids.to_alipay_dict()
            else:
                params['shop_ids'] = self.shop_ids
        if self.threshold_amount:
            if hasattr(self.threshold_amount, 'to_alipay_dict'):
                params['threshold_amount'] = self.threshold_amount.to_alipay_dict()
            else:
                params['threshold_amount'] = self.threshold_amount
        if self.total_inventory:
            if hasattr(self.total_inventory, 'to_alipay_dict'):
                params['total_inventory'] = self.total_inventory.to_alipay_dict()
            else:
                params['total_inventory'] = self.total_inventory
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        if self.voucher_name:
            if hasattr(self.voucher_name, 'to_alipay_dict'):
                params['voucher_name'] = self.voucher_name.to_alipay_dict()
            else:
                params['voucher_name'] = self.voucher_name
        if self.voucher_org_value:
            if hasattr(self.voucher_org_value, 'to_alipay_dict'):
                params['voucher_org_value'] = self.voucher_org_value.to_alipay_dict()
            else:
                params['voucher_org_value'] = self.voucher_org_value
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        if self.voucher_value:
            if hasattr(self.voucher_value, 'to_alipay_dict'):
                params['voucher_value'] = self.voucher_value.to_alipay_dict()
            else:
                params['voucher_value'] = self.voucher_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertSubjectVoucherResponse()
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'city_ids' in d:
            o.city_ids = d['city_ids']
        if 'cover' in d:
            o.cover = d['cover']
        if 'daily_inventory' in d:
            o.daily_inventory = d['daily_inventory']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'gmt_start' in d:
            o.gmt_start = d['gmt_start']
        if 'logo' in d:
            o.logo = d['logo']
        if 'manuals' in d:
            o.manuals = d['manuals']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'purchase_mode' in d:
            o.purchase_mode = d['purchase_mode']
        if 'shop_ids' in d:
            o.shop_ids = d['shop_ids']
        if 'threshold_amount' in d:
            o.threshold_amount = d['threshold_amount']
        if 'total_inventory' in d:
            o.total_inventory = d['total_inventory']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        if 'voucher_name' in d:
            o.voucher_name = d['voucher_name']
        if 'voucher_org_value' in d:
            o.voucher_org_value = d['voucher_org_value']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        if 'voucher_value' in d:
            o.voucher_value = d['voucher_value']
        return o


