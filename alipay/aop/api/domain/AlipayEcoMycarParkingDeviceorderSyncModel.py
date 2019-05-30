#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarParkingDeviceorderSyncModel(object):

    def __init__(self):
        self._alipay_parking_id = None
        self._alipay_supplier_sn = None
        self._applicant_alipay_account = None
        self._applicant_name = None
        self._applicant_phone = None
        self._biz_time = None
        self._booth_num = None
        self._device_num = None
        self._device_type = None
        self._order_id = None
        self._order_state = None
        self._pklot_principal_name = None
        self._pklot_principal_phone = None
        self._receiver_address = None
        self._receiver_name = None
        self._receiver_phone = None
        self._remarks = None

    @property
    def alipay_parking_id(self):
        return self._alipay_parking_id

    @alipay_parking_id.setter
    def alipay_parking_id(self, value):
        self._alipay_parking_id = value
    @property
    def alipay_supplier_sn(self):
        return self._alipay_supplier_sn

    @alipay_supplier_sn.setter
    def alipay_supplier_sn(self, value):
        self._alipay_supplier_sn = value
    @property
    def applicant_alipay_account(self):
        return self._applicant_alipay_account

    @applicant_alipay_account.setter
    def applicant_alipay_account(self, value):
        self._applicant_alipay_account = value
    @property
    def applicant_name(self):
        return self._applicant_name

    @applicant_name.setter
    def applicant_name(self, value):
        self._applicant_name = value
    @property
    def applicant_phone(self):
        return self._applicant_phone

    @applicant_phone.setter
    def applicant_phone(self, value):
        self._applicant_phone = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def booth_num(self):
        return self._booth_num

    @booth_num.setter
    def booth_num(self, value):
        self._booth_num = value
    @property
    def device_num(self):
        return self._device_num

    @device_num.setter
    def device_num(self, value):
        self._device_num = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_state(self):
        return self._order_state

    @order_state.setter
    def order_state(self, value):
        self._order_state = value
    @property
    def pklot_principal_name(self):
        return self._pklot_principal_name

    @pklot_principal_name.setter
    def pklot_principal_name(self, value):
        self._pklot_principal_name = value
    @property
    def pklot_principal_phone(self):
        return self._pklot_principal_phone

    @pklot_principal_phone.setter
    def pklot_principal_phone(self, value):
        self._pklot_principal_phone = value
    @property
    def receiver_address(self):
        return self._receiver_address

    @receiver_address.setter
    def receiver_address(self, value):
        self._receiver_address = value
    @property
    def receiver_name(self):
        return self._receiver_name

    @receiver_name.setter
    def receiver_name(self, value):
        self._receiver_name = value
    @property
    def receiver_phone(self):
        return self._receiver_phone

    @receiver_phone.setter
    def receiver_phone(self, value):
        self._receiver_phone = value
    @property
    def remarks(self):
        return self._remarks

    @remarks.setter
    def remarks(self, value):
        self._remarks = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_parking_id:
            if hasattr(self.alipay_parking_id, 'to_alipay_dict'):
                params['alipay_parking_id'] = self.alipay_parking_id.to_alipay_dict()
            else:
                params['alipay_parking_id'] = self.alipay_parking_id
        if self.alipay_supplier_sn:
            if hasattr(self.alipay_supplier_sn, 'to_alipay_dict'):
                params['alipay_supplier_sn'] = self.alipay_supplier_sn.to_alipay_dict()
            else:
                params['alipay_supplier_sn'] = self.alipay_supplier_sn
        if self.applicant_alipay_account:
            if hasattr(self.applicant_alipay_account, 'to_alipay_dict'):
                params['applicant_alipay_account'] = self.applicant_alipay_account.to_alipay_dict()
            else:
                params['applicant_alipay_account'] = self.applicant_alipay_account
        if self.applicant_name:
            if hasattr(self.applicant_name, 'to_alipay_dict'):
                params['applicant_name'] = self.applicant_name.to_alipay_dict()
            else:
                params['applicant_name'] = self.applicant_name
        if self.applicant_phone:
            if hasattr(self.applicant_phone, 'to_alipay_dict'):
                params['applicant_phone'] = self.applicant_phone.to_alipay_dict()
            else:
                params['applicant_phone'] = self.applicant_phone
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.booth_num:
            if hasattr(self.booth_num, 'to_alipay_dict'):
                params['booth_num'] = self.booth_num.to_alipay_dict()
            else:
                params['booth_num'] = self.booth_num
        if self.device_num:
            if hasattr(self.device_num, 'to_alipay_dict'):
                params['device_num'] = self.device_num.to_alipay_dict()
            else:
                params['device_num'] = self.device_num
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_state:
            if hasattr(self.order_state, 'to_alipay_dict'):
                params['order_state'] = self.order_state.to_alipay_dict()
            else:
                params['order_state'] = self.order_state
        if self.pklot_principal_name:
            if hasattr(self.pklot_principal_name, 'to_alipay_dict'):
                params['pklot_principal_name'] = self.pklot_principal_name.to_alipay_dict()
            else:
                params['pklot_principal_name'] = self.pklot_principal_name
        if self.pklot_principal_phone:
            if hasattr(self.pklot_principal_phone, 'to_alipay_dict'):
                params['pklot_principal_phone'] = self.pklot_principal_phone.to_alipay_dict()
            else:
                params['pklot_principal_phone'] = self.pklot_principal_phone
        if self.receiver_address:
            if hasattr(self.receiver_address, 'to_alipay_dict'):
                params['receiver_address'] = self.receiver_address.to_alipay_dict()
            else:
                params['receiver_address'] = self.receiver_address
        if self.receiver_name:
            if hasattr(self.receiver_name, 'to_alipay_dict'):
                params['receiver_name'] = self.receiver_name.to_alipay_dict()
            else:
                params['receiver_name'] = self.receiver_name
        if self.receiver_phone:
            if hasattr(self.receiver_phone, 'to_alipay_dict'):
                params['receiver_phone'] = self.receiver_phone.to_alipay_dict()
            else:
                params['receiver_phone'] = self.receiver_phone
        if self.remarks:
            if hasattr(self.remarks, 'to_alipay_dict'):
                params['remarks'] = self.remarks.to_alipay_dict()
            else:
                params['remarks'] = self.remarks
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarParkingDeviceorderSyncModel()
        if 'alipay_parking_id' in d:
            o.alipay_parking_id = d['alipay_parking_id']
        if 'alipay_supplier_sn' in d:
            o.alipay_supplier_sn = d['alipay_supplier_sn']
        if 'applicant_alipay_account' in d:
            o.applicant_alipay_account = d['applicant_alipay_account']
        if 'applicant_name' in d:
            o.applicant_name = d['applicant_name']
        if 'applicant_phone' in d:
            o.applicant_phone = d['applicant_phone']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'booth_num' in d:
            o.booth_num = d['booth_num']
        if 'device_num' in d:
            o.device_num = d['device_num']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_state' in d:
            o.order_state = d['order_state']
        if 'pklot_principal_name' in d:
            o.pklot_principal_name = d['pklot_principal_name']
        if 'pklot_principal_phone' in d:
            o.pklot_principal_phone = d['pklot_principal_phone']
        if 'receiver_address' in d:
            o.receiver_address = d['receiver_address']
        if 'receiver_name' in d:
            o.receiver_name = d['receiver_name']
        if 'receiver_phone' in d:
            o.receiver_phone = d['receiver_phone']
        if 'remarks' in d:
            o.remarks = d['remarks']
        return o


