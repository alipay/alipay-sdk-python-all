#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EcomLogisticsOrderDTO(object):

    def __init__(self):
        self._company_code = None
        self._company_name = None
        self._consign_time = None
        self._end_time = None
        self._logistics_no = None
        self._logistics_order_id = None
        self._logistics_status = None
        self._post_fee = None
        self._recipient_address = None
        self._recipient_area = None
        self._recipient_area_code = None
        self._recipient_city = None
        self._recipient_full_name = None
        self._recipient_mobile_phone = None
        self._recipient_phone = None
        self._recipient_prov = None
        self._recipient_town = None
        self._refusal = None
        self._sender_address = None
        self._sender_area = None
        self._sender_area_code = None
        self._sender_city = None
        self._sender_full_name = None
        self._sender_mobile_phone = None
        self._sender_phone = None
        self._sender_prov = None
        self._sender_town = None

    @property
    def company_code(self):
        return self._company_code

    @company_code.setter
    def company_code(self, value):
        self._company_code = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def consign_time(self):
        return self._consign_time

    @consign_time.setter
    def consign_time(self, value):
        self._consign_time = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def logistics_no(self):
        return self._logistics_no

    @logistics_no.setter
    def logistics_no(self, value):
        self._logistics_no = value
    @property
    def logistics_order_id(self):
        return self._logistics_order_id

    @logistics_order_id.setter
    def logistics_order_id(self, value):
        self._logistics_order_id = value
    @property
    def logistics_status(self):
        return self._logistics_status

    @logistics_status.setter
    def logistics_status(self, value):
        self._logistics_status = value
    @property
    def post_fee(self):
        return self._post_fee

    @post_fee.setter
    def post_fee(self, value):
        self._post_fee = value
    @property
    def recipient_address(self):
        return self._recipient_address

    @recipient_address.setter
    def recipient_address(self, value):
        self._recipient_address = value
    @property
    def recipient_area(self):
        return self._recipient_area

    @recipient_area.setter
    def recipient_area(self, value):
        self._recipient_area = value
    @property
    def recipient_area_code(self):
        return self._recipient_area_code

    @recipient_area_code.setter
    def recipient_area_code(self, value):
        self._recipient_area_code = value
    @property
    def recipient_city(self):
        return self._recipient_city

    @recipient_city.setter
    def recipient_city(self, value):
        self._recipient_city = value
    @property
    def recipient_full_name(self):
        return self._recipient_full_name

    @recipient_full_name.setter
    def recipient_full_name(self, value):
        self._recipient_full_name = value
    @property
    def recipient_mobile_phone(self):
        return self._recipient_mobile_phone

    @recipient_mobile_phone.setter
    def recipient_mobile_phone(self, value):
        self._recipient_mobile_phone = value
    @property
    def recipient_phone(self):
        return self._recipient_phone

    @recipient_phone.setter
    def recipient_phone(self, value):
        self._recipient_phone = value
    @property
    def recipient_prov(self):
        return self._recipient_prov

    @recipient_prov.setter
    def recipient_prov(self, value):
        self._recipient_prov = value
    @property
    def recipient_town(self):
        return self._recipient_town

    @recipient_town.setter
    def recipient_town(self, value):
        self._recipient_town = value
    @property
    def refusal(self):
        return self._refusal

    @refusal.setter
    def refusal(self, value):
        self._refusal = value
    @property
    def sender_address(self):
        return self._sender_address

    @sender_address.setter
    def sender_address(self, value):
        self._sender_address = value
    @property
    def sender_area(self):
        return self._sender_area

    @sender_area.setter
    def sender_area(self, value):
        self._sender_area = value
    @property
    def sender_area_code(self):
        return self._sender_area_code

    @sender_area_code.setter
    def sender_area_code(self, value):
        self._sender_area_code = value
    @property
    def sender_city(self):
        return self._sender_city

    @sender_city.setter
    def sender_city(self, value):
        self._sender_city = value
    @property
    def sender_full_name(self):
        return self._sender_full_name

    @sender_full_name.setter
    def sender_full_name(self, value):
        self._sender_full_name = value
    @property
    def sender_mobile_phone(self):
        return self._sender_mobile_phone

    @sender_mobile_phone.setter
    def sender_mobile_phone(self, value):
        self._sender_mobile_phone = value
    @property
    def sender_phone(self):
        return self._sender_phone

    @sender_phone.setter
    def sender_phone(self, value):
        self._sender_phone = value
    @property
    def sender_prov(self):
        return self._sender_prov

    @sender_prov.setter
    def sender_prov(self, value):
        self._sender_prov = value
    @property
    def sender_town(self):
        return self._sender_town

    @sender_town.setter
    def sender_town(self, value):
        self._sender_town = value


    def to_alipay_dict(self):
        params = dict()
        if self.company_code:
            if hasattr(self.company_code, 'to_alipay_dict'):
                params['company_code'] = self.company_code.to_alipay_dict()
            else:
                params['company_code'] = self.company_code
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.consign_time:
            if hasattr(self.consign_time, 'to_alipay_dict'):
                params['consign_time'] = self.consign_time.to_alipay_dict()
            else:
                params['consign_time'] = self.consign_time
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.logistics_no:
            if hasattr(self.logistics_no, 'to_alipay_dict'):
                params['logistics_no'] = self.logistics_no.to_alipay_dict()
            else:
                params['logistics_no'] = self.logistics_no
        if self.logistics_order_id:
            if hasattr(self.logistics_order_id, 'to_alipay_dict'):
                params['logistics_order_id'] = self.logistics_order_id.to_alipay_dict()
            else:
                params['logistics_order_id'] = self.logistics_order_id
        if self.logistics_status:
            if hasattr(self.logistics_status, 'to_alipay_dict'):
                params['logistics_status'] = self.logistics_status.to_alipay_dict()
            else:
                params['logistics_status'] = self.logistics_status
        if self.post_fee:
            if hasattr(self.post_fee, 'to_alipay_dict'):
                params['post_fee'] = self.post_fee.to_alipay_dict()
            else:
                params['post_fee'] = self.post_fee
        if self.recipient_address:
            if hasattr(self.recipient_address, 'to_alipay_dict'):
                params['recipient_address'] = self.recipient_address.to_alipay_dict()
            else:
                params['recipient_address'] = self.recipient_address
        if self.recipient_area:
            if hasattr(self.recipient_area, 'to_alipay_dict'):
                params['recipient_area'] = self.recipient_area.to_alipay_dict()
            else:
                params['recipient_area'] = self.recipient_area
        if self.recipient_area_code:
            if hasattr(self.recipient_area_code, 'to_alipay_dict'):
                params['recipient_area_code'] = self.recipient_area_code.to_alipay_dict()
            else:
                params['recipient_area_code'] = self.recipient_area_code
        if self.recipient_city:
            if hasattr(self.recipient_city, 'to_alipay_dict'):
                params['recipient_city'] = self.recipient_city.to_alipay_dict()
            else:
                params['recipient_city'] = self.recipient_city
        if self.recipient_full_name:
            if hasattr(self.recipient_full_name, 'to_alipay_dict'):
                params['recipient_full_name'] = self.recipient_full_name.to_alipay_dict()
            else:
                params['recipient_full_name'] = self.recipient_full_name
        if self.recipient_mobile_phone:
            if hasattr(self.recipient_mobile_phone, 'to_alipay_dict'):
                params['recipient_mobile_phone'] = self.recipient_mobile_phone.to_alipay_dict()
            else:
                params['recipient_mobile_phone'] = self.recipient_mobile_phone
        if self.recipient_phone:
            if hasattr(self.recipient_phone, 'to_alipay_dict'):
                params['recipient_phone'] = self.recipient_phone.to_alipay_dict()
            else:
                params['recipient_phone'] = self.recipient_phone
        if self.recipient_prov:
            if hasattr(self.recipient_prov, 'to_alipay_dict'):
                params['recipient_prov'] = self.recipient_prov.to_alipay_dict()
            else:
                params['recipient_prov'] = self.recipient_prov
        if self.recipient_town:
            if hasattr(self.recipient_town, 'to_alipay_dict'):
                params['recipient_town'] = self.recipient_town.to_alipay_dict()
            else:
                params['recipient_town'] = self.recipient_town
        if self.refusal:
            if hasattr(self.refusal, 'to_alipay_dict'):
                params['refusal'] = self.refusal.to_alipay_dict()
            else:
                params['refusal'] = self.refusal
        if self.sender_address:
            if hasattr(self.sender_address, 'to_alipay_dict'):
                params['sender_address'] = self.sender_address.to_alipay_dict()
            else:
                params['sender_address'] = self.sender_address
        if self.sender_area:
            if hasattr(self.sender_area, 'to_alipay_dict'):
                params['sender_area'] = self.sender_area.to_alipay_dict()
            else:
                params['sender_area'] = self.sender_area
        if self.sender_area_code:
            if hasattr(self.sender_area_code, 'to_alipay_dict'):
                params['sender_area_code'] = self.sender_area_code.to_alipay_dict()
            else:
                params['sender_area_code'] = self.sender_area_code
        if self.sender_city:
            if hasattr(self.sender_city, 'to_alipay_dict'):
                params['sender_city'] = self.sender_city.to_alipay_dict()
            else:
                params['sender_city'] = self.sender_city
        if self.sender_full_name:
            if hasattr(self.sender_full_name, 'to_alipay_dict'):
                params['sender_full_name'] = self.sender_full_name.to_alipay_dict()
            else:
                params['sender_full_name'] = self.sender_full_name
        if self.sender_mobile_phone:
            if hasattr(self.sender_mobile_phone, 'to_alipay_dict'):
                params['sender_mobile_phone'] = self.sender_mobile_phone.to_alipay_dict()
            else:
                params['sender_mobile_phone'] = self.sender_mobile_phone
        if self.sender_phone:
            if hasattr(self.sender_phone, 'to_alipay_dict'):
                params['sender_phone'] = self.sender_phone.to_alipay_dict()
            else:
                params['sender_phone'] = self.sender_phone
        if self.sender_prov:
            if hasattr(self.sender_prov, 'to_alipay_dict'):
                params['sender_prov'] = self.sender_prov.to_alipay_dict()
            else:
                params['sender_prov'] = self.sender_prov
        if self.sender_town:
            if hasattr(self.sender_town, 'to_alipay_dict'):
                params['sender_town'] = self.sender_town.to_alipay_dict()
            else:
                params['sender_town'] = self.sender_town
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcomLogisticsOrderDTO()
        if 'company_code' in d:
            o.company_code = d['company_code']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'consign_time' in d:
            o.consign_time = d['consign_time']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'logistics_no' in d:
            o.logistics_no = d['logistics_no']
        if 'logistics_order_id' in d:
            o.logistics_order_id = d['logistics_order_id']
        if 'logistics_status' in d:
            o.logistics_status = d['logistics_status']
        if 'post_fee' in d:
            o.post_fee = d['post_fee']
        if 'recipient_address' in d:
            o.recipient_address = d['recipient_address']
        if 'recipient_area' in d:
            o.recipient_area = d['recipient_area']
        if 'recipient_area_code' in d:
            o.recipient_area_code = d['recipient_area_code']
        if 'recipient_city' in d:
            o.recipient_city = d['recipient_city']
        if 'recipient_full_name' in d:
            o.recipient_full_name = d['recipient_full_name']
        if 'recipient_mobile_phone' in d:
            o.recipient_mobile_phone = d['recipient_mobile_phone']
        if 'recipient_phone' in d:
            o.recipient_phone = d['recipient_phone']
        if 'recipient_prov' in d:
            o.recipient_prov = d['recipient_prov']
        if 'recipient_town' in d:
            o.recipient_town = d['recipient_town']
        if 'refusal' in d:
            o.refusal = d['refusal']
        if 'sender_address' in d:
            o.sender_address = d['sender_address']
        if 'sender_area' in d:
            o.sender_area = d['sender_area']
        if 'sender_area_code' in d:
            o.sender_area_code = d['sender_area_code']
        if 'sender_city' in d:
            o.sender_city = d['sender_city']
        if 'sender_full_name' in d:
            o.sender_full_name = d['sender_full_name']
        if 'sender_mobile_phone' in d:
            o.sender_mobile_phone = d['sender_mobile_phone']
        if 'sender_phone' in d:
            o.sender_phone = d['sender_phone']
        if 'sender_prov' in d:
            o.sender_prov = d['sender_prov']
        if 'sender_town' in d:
            o.sender_town = d['sender_town']
        return o


