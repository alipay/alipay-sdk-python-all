#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderBroadcastReportDownloadModel(object):

    def __init__(self):
        self._device_sn = None
        self._report_dt = None
        self._smid = None

    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def report_dt(self):
        return self._report_dt

    @report_dt.setter
    def report_dt(self, value):
        self._report_dt = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.report_dt:
            if hasattr(self.report_dt, 'to_alipay_dict'):
                params['report_dt'] = self.report_dt.to_alipay_dict()
            else:
                params['report_dt'] = self.report_dt
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderBroadcastReportDownloadModel()
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'report_dt' in d:
            o.report_dt = d['report_dt']
        if 'smid' in d:
            o.smid = d['smid']
        return o


