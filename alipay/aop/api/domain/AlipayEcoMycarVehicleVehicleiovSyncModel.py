#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VehicleIovData import VehicleIovData


class AlipayEcoMycarVehicleVehicleiovSyncModel(object):

    def __init__(self):
        self._ext_info = None
        self._iov_datas = None
        self._iov_seq_no = None
        self._system_timestamp = None
        self._user_id = None
        self._vehicle_open_id = None
        self._vi_id = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def iov_datas(self):
        return self._iov_datas

    @iov_datas.setter
    def iov_datas(self, value):
        if isinstance(value, list):
            self._iov_datas = list()
            for i in value:
                if isinstance(i, VehicleIovData):
                    self._iov_datas.append(i)
                else:
                    self._iov_datas.append(VehicleIovData.from_alipay_dict(i))
    @property
    def iov_seq_no(self):
        return self._iov_seq_no

    @iov_seq_no.setter
    def iov_seq_no(self, value):
        self._iov_seq_no = value
    @property
    def system_timestamp(self):
        return self._system_timestamp

    @system_timestamp.setter
    def system_timestamp(self, value):
        self._system_timestamp = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def vehicle_open_id(self):
        return self._vehicle_open_id

    @vehicle_open_id.setter
    def vehicle_open_id(self, value):
        self._vehicle_open_id = value
    @property
    def vi_id(self):
        return self._vi_id

    @vi_id.setter
    def vi_id(self, value):
        self._vi_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.iov_datas:
            if isinstance(self.iov_datas, list):
                for i in range(0, len(self.iov_datas)):
                    element = self.iov_datas[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.iov_datas[i] = element.to_alipay_dict()
            if hasattr(self.iov_datas, 'to_alipay_dict'):
                params['iov_datas'] = self.iov_datas.to_alipay_dict()
            else:
                params['iov_datas'] = self.iov_datas
        if self.iov_seq_no:
            if hasattr(self.iov_seq_no, 'to_alipay_dict'):
                params['iov_seq_no'] = self.iov_seq_no.to_alipay_dict()
            else:
                params['iov_seq_no'] = self.iov_seq_no
        if self.system_timestamp:
            if hasattr(self.system_timestamp, 'to_alipay_dict'):
                params['system_timestamp'] = self.system_timestamp.to_alipay_dict()
            else:
                params['system_timestamp'] = self.system_timestamp
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.vehicle_open_id:
            if hasattr(self.vehicle_open_id, 'to_alipay_dict'):
                params['vehicle_open_id'] = self.vehicle_open_id.to_alipay_dict()
            else:
                params['vehicle_open_id'] = self.vehicle_open_id
        if self.vi_id:
            if hasattr(self.vi_id, 'to_alipay_dict'):
                params['vi_id'] = self.vi_id.to_alipay_dict()
            else:
                params['vi_id'] = self.vi_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarVehicleVehicleiovSyncModel()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'iov_datas' in d:
            o.iov_datas = d['iov_datas']
        if 'iov_seq_no' in d:
            o.iov_seq_no = d['iov_seq_no']
        if 'system_timestamp' in d:
            o.system_timestamp = d['system_timestamp']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'vehicle_open_id' in d:
            o.vehicle_open_id = d['vehicle_open_id']
        if 'vi_id' in d:
            o.vi_id = d['vi_id']
        return o


