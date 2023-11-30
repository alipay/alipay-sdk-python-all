#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PointAddressInfo import PointAddressInfo
from alipay.aop.api.domain.PointBusinessTime import PointBusinessTime


class PointInfo(object):

    def __init__(self):
        self._address = None
        self._business_time = None
        self._contact_mobile = None
        self._contact_phone = None
        self._device_sn = None
        self._out_device_point_id = None
        self._point_category_code = None
        self._point_group = None
        self._point_name = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if isinstance(value, PointAddressInfo):
            self._address = value
        else:
            self._address = PointAddressInfo.from_alipay_dict(value)
    @property
    def business_time(self):
        return self._business_time

    @business_time.setter
    def business_time(self, value):
        if isinstance(value, list):
            self._business_time = list()
            for i in value:
                if isinstance(i, PointBusinessTime):
                    self._business_time.append(i)
                else:
                    self._business_time.append(PointBusinessTime.from_alipay_dict(i))
    @property
    def contact_mobile(self):
        return self._contact_mobile

    @contact_mobile.setter
    def contact_mobile(self, value):
        self._contact_mobile = value
    @property
    def contact_phone(self):
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, value):
        self._contact_phone = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def out_device_point_id(self):
        return self._out_device_point_id

    @out_device_point_id.setter
    def out_device_point_id(self, value):
        self._out_device_point_id = value
    @property
    def point_category_code(self):
        return self._point_category_code

    @point_category_code.setter
    def point_category_code(self, value):
        self._point_category_code = value
    @property
    def point_group(self):
        return self._point_group

    @point_group.setter
    def point_group(self, value):
        self._point_group = value
    @property
    def point_name(self):
        return self._point_name

    @point_name.setter
    def point_name(self, value):
        self._point_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.business_time:
            if isinstance(self.business_time, list):
                for i in range(0, len(self.business_time)):
                    element = self.business_time[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.business_time[i] = element.to_alipay_dict()
            if hasattr(self.business_time, 'to_alipay_dict'):
                params['business_time'] = self.business_time.to_alipay_dict()
            else:
                params['business_time'] = self.business_time
        if self.contact_mobile:
            if hasattr(self.contact_mobile, 'to_alipay_dict'):
                params['contact_mobile'] = self.contact_mobile.to_alipay_dict()
            else:
                params['contact_mobile'] = self.contact_mobile
        if self.contact_phone:
            if hasattr(self.contact_phone, 'to_alipay_dict'):
                params['contact_phone'] = self.contact_phone.to_alipay_dict()
            else:
                params['contact_phone'] = self.contact_phone
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.out_device_point_id:
            if hasattr(self.out_device_point_id, 'to_alipay_dict'):
                params['out_device_point_id'] = self.out_device_point_id.to_alipay_dict()
            else:
                params['out_device_point_id'] = self.out_device_point_id
        if self.point_category_code:
            if hasattr(self.point_category_code, 'to_alipay_dict'):
                params['point_category_code'] = self.point_category_code.to_alipay_dict()
            else:
                params['point_category_code'] = self.point_category_code
        if self.point_group:
            if hasattr(self.point_group, 'to_alipay_dict'):
                params['point_group'] = self.point_group.to_alipay_dict()
            else:
                params['point_group'] = self.point_group
        if self.point_name:
            if hasattr(self.point_name, 'to_alipay_dict'):
                params['point_name'] = self.point_name.to_alipay_dict()
            else:
                params['point_name'] = self.point_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PointInfo()
        if 'address' in d:
            o.address = d['address']
        if 'business_time' in d:
            o.business_time = d['business_time']
        if 'contact_mobile' in d:
            o.contact_mobile = d['contact_mobile']
        if 'contact_phone' in d:
            o.contact_phone = d['contact_phone']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'out_device_point_id' in d:
            o.out_device_point_id = d['out_device_point_id']
        if 'point_category_code' in d:
            o.point_category_code = d['point_category_code']
        if 'point_group' in d:
            o.point_group = d['point_group']
        if 'point_name' in d:
            o.point_name = d['point_name']
        return o


