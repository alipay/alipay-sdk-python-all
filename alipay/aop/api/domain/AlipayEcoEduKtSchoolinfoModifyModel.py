#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoEduKtSchoolinfoModifyModel(object):

    def __init__(self):
        self._bank_notify_url = None
        self._bank_partner_id = None
        self._bank_uid = None
        self._bankcard_no = None
        self._batch_no = None
        self._card_alias_no = None
        self._city_code = None
        self._city_name = None
        self._corporate_branch_pid = None
        self._district_code = None
        self._district_name = None
        self._isv_name = None
        self._isv_no = None
        self._isv_notify_url = None
        self._isv_phone = None
        self._isv_pid = None
        self._province_code = None
        self._province_name = None
        self._school_icon = None
        self._school_icon_type = None
        self._school_name = None
        self._school_pid = None
        self._school_stdcode = None
        self._school_type = None
        self._smid = None
        self._trans_in = None
        self._white_channel_code = None

    @property
    def bank_notify_url(self):
        return self._bank_notify_url

    @bank_notify_url.setter
    def bank_notify_url(self, value):
        self._bank_notify_url = value
    @property
    def bank_partner_id(self):
        return self._bank_partner_id

    @bank_partner_id.setter
    def bank_partner_id(self, value):
        self._bank_partner_id = value
    @property
    def bank_uid(self):
        return self._bank_uid

    @bank_uid.setter
    def bank_uid(self, value):
        self._bank_uid = value
    @property
    def bankcard_no(self):
        return self._bankcard_no

    @bankcard_no.setter
    def bankcard_no(self, value):
        self._bankcard_no = value
    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def card_alias_no(self):
        return self._card_alias_no

    @card_alias_no.setter
    def card_alias_no(self, value):
        self._card_alias_no = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def corporate_branch_pid(self):
        return self._corporate_branch_pid

    @corporate_branch_pid.setter
    def corporate_branch_pid(self, value):
        self._corporate_branch_pid = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def district_name(self):
        return self._district_name

    @district_name.setter
    def district_name(self, value):
        self._district_name = value
    @property
    def isv_name(self):
        return self._isv_name

    @isv_name.setter
    def isv_name(self, value):
        self._isv_name = value
    @property
    def isv_no(self):
        return self._isv_no

    @isv_no.setter
    def isv_no(self, value):
        self._isv_no = value
    @property
    def isv_notify_url(self):
        return self._isv_notify_url

    @isv_notify_url.setter
    def isv_notify_url(self, value):
        self._isv_notify_url = value
    @property
    def isv_phone(self):
        return self._isv_phone

    @isv_phone.setter
    def isv_phone(self, value):
        self._isv_phone = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value
    @property
    def school_icon(self):
        return self._school_icon

    @school_icon.setter
    def school_icon(self, value):
        self._school_icon = value
    @property
    def school_icon_type(self):
        return self._school_icon_type

    @school_icon_type.setter
    def school_icon_type(self, value):
        self._school_icon_type = value
    @property
    def school_name(self):
        return self._school_name

    @school_name.setter
    def school_name(self, value):
        self._school_name = value
    @property
    def school_pid(self):
        return self._school_pid

    @school_pid.setter
    def school_pid(self, value):
        self._school_pid = value
    @property
    def school_stdcode(self):
        return self._school_stdcode

    @school_stdcode.setter
    def school_stdcode(self, value):
        self._school_stdcode = value
    @property
    def school_type(self):
        return self._school_type

    @school_type.setter
    def school_type(self, value):
        self._school_type = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def trans_in(self):
        return self._trans_in

    @trans_in.setter
    def trans_in(self, value):
        self._trans_in = value
    @property
    def white_channel_code(self):
        return self._white_channel_code

    @white_channel_code.setter
    def white_channel_code(self, value):
        self._white_channel_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_notify_url:
            if hasattr(self.bank_notify_url, 'to_alipay_dict'):
                params['bank_notify_url'] = self.bank_notify_url.to_alipay_dict()
            else:
                params['bank_notify_url'] = self.bank_notify_url
        if self.bank_partner_id:
            if hasattr(self.bank_partner_id, 'to_alipay_dict'):
                params['bank_partner_id'] = self.bank_partner_id.to_alipay_dict()
            else:
                params['bank_partner_id'] = self.bank_partner_id
        if self.bank_uid:
            if hasattr(self.bank_uid, 'to_alipay_dict'):
                params['bank_uid'] = self.bank_uid.to_alipay_dict()
            else:
                params['bank_uid'] = self.bank_uid
        if self.bankcard_no:
            if hasattr(self.bankcard_no, 'to_alipay_dict'):
                params['bankcard_no'] = self.bankcard_no.to_alipay_dict()
            else:
                params['bankcard_no'] = self.bankcard_no
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.card_alias_no:
            if hasattr(self.card_alias_no, 'to_alipay_dict'):
                params['card_alias_no'] = self.card_alias_no.to_alipay_dict()
            else:
                params['card_alias_no'] = self.card_alias_no
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.corporate_branch_pid:
            if hasattr(self.corporate_branch_pid, 'to_alipay_dict'):
                params['corporate_branch_pid'] = self.corporate_branch_pid.to_alipay_dict()
            else:
                params['corporate_branch_pid'] = self.corporate_branch_pid
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.district_name:
            if hasattr(self.district_name, 'to_alipay_dict'):
                params['district_name'] = self.district_name.to_alipay_dict()
            else:
                params['district_name'] = self.district_name
        if self.isv_name:
            if hasattr(self.isv_name, 'to_alipay_dict'):
                params['isv_name'] = self.isv_name.to_alipay_dict()
            else:
                params['isv_name'] = self.isv_name
        if self.isv_no:
            if hasattr(self.isv_no, 'to_alipay_dict'):
                params['isv_no'] = self.isv_no.to_alipay_dict()
            else:
                params['isv_no'] = self.isv_no
        if self.isv_notify_url:
            if hasattr(self.isv_notify_url, 'to_alipay_dict'):
                params['isv_notify_url'] = self.isv_notify_url.to_alipay_dict()
            else:
                params['isv_notify_url'] = self.isv_notify_url
        if self.isv_phone:
            if hasattr(self.isv_phone, 'to_alipay_dict'):
                params['isv_phone'] = self.isv_phone.to_alipay_dict()
            else:
                params['isv_phone'] = self.isv_phone
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.province_name:
            if hasattr(self.province_name, 'to_alipay_dict'):
                params['province_name'] = self.province_name.to_alipay_dict()
            else:
                params['province_name'] = self.province_name
        if self.school_icon:
            if hasattr(self.school_icon, 'to_alipay_dict'):
                params['school_icon'] = self.school_icon.to_alipay_dict()
            else:
                params['school_icon'] = self.school_icon
        if self.school_icon_type:
            if hasattr(self.school_icon_type, 'to_alipay_dict'):
                params['school_icon_type'] = self.school_icon_type.to_alipay_dict()
            else:
                params['school_icon_type'] = self.school_icon_type
        if self.school_name:
            if hasattr(self.school_name, 'to_alipay_dict'):
                params['school_name'] = self.school_name.to_alipay_dict()
            else:
                params['school_name'] = self.school_name
        if self.school_pid:
            if hasattr(self.school_pid, 'to_alipay_dict'):
                params['school_pid'] = self.school_pid.to_alipay_dict()
            else:
                params['school_pid'] = self.school_pid
        if self.school_stdcode:
            if hasattr(self.school_stdcode, 'to_alipay_dict'):
                params['school_stdcode'] = self.school_stdcode.to_alipay_dict()
            else:
                params['school_stdcode'] = self.school_stdcode
        if self.school_type:
            if hasattr(self.school_type, 'to_alipay_dict'):
                params['school_type'] = self.school_type.to_alipay_dict()
            else:
                params['school_type'] = self.school_type
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.trans_in:
            if hasattr(self.trans_in, 'to_alipay_dict'):
                params['trans_in'] = self.trans_in.to_alipay_dict()
            else:
                params['trans_in'] = self.trans_in
        if self.white_channel_code:
            if hasattr(self.white_channel_code, 'to_alipay_dict'):
                params['white_channel_code'] = self.white_channel_code.to_alipay_dict()
            else:
                params['white_channel_code'] = self.white_channel_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoEduKtSchoolinfoModifyModel()
        if 'bank_notify_url' in d:
            o.bank_notify_url = d['bank_notify_url']
        if 'bank_partner_id' in d:
            o.bank_partner_id = d['bank_partner_id']
        if 'bank_uid' in d:
            o.bank_uid = d['bank_uid']
        if 'bankcard_no' in d:
            o.bankcard_no = d['bankcard_no']
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'card_alias_no' in d:
            o.card_alias_no = d['card_alias_no']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'corporate_branch_pid' in d:
            o.corporate_branch_pid = d['corporate_branch_pid']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'district_name' in d:
            o.district_name = d['district_name']
        if 'isv_name' in d:
            o.isv_name = d['isv_name']
        if 'isv_no' in d:
            o.isv_no = d['isv_no']
        if 'isv_notify_url' in d:
            o.isv_notify_url = d['isv_notify_url']
        if 'isv_phone' in d:
            o.isv_phone = d['isv_phone']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'province_name' in d:
            o.province_name = d['province_name']
        if 'school_icon' in d:
            o.school_icon = d['school_icon']
        if 'school_icon_type' in d:
            o.school_icon_type = d['school_icon_type']
        if 'school_name' in d:
            o.school_name = d['school_name']
        if 'school_pid' in d:
            o.school_pid = d['school_pid']
        if 'school_stdcode' in d:
            o.school_stdcode = d['school_stdcode']
        if 'school_type' in d:
            o.school_type = d['school_type']
        if 'smid' in d:
            o.smid = d['smid']
        if 'trans_in' in d:
            o.trans_in = d['trans_in']
        if 'white_channel_code' in d:
            o.white_channel_code = d['white_channel_code']
        return o


