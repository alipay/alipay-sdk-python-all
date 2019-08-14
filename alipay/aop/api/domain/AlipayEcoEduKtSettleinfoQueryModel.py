#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoEduKtSettleinfoQueryModel(object):

    def __init__(self):
        self._bill_date = None
        self._partner_pid = None
        self._school_no = None
        self._smid = None

    @property
    def bill_date(self):
        return self._bill_date

    @bill_date.setter
    def bill_date(self, value):
        self._bill_date = value
    @property
    def partner_pid(self):
        return self._partner_pid

    @partner_pid.setter
    def partner_pid(self, value):
        self._partner_pid = value
    @property
    def school_no(self):
        return self._school_no

    @school_no.setter
    def school_no(self, value):
        self._school_no = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_date:
            if hasattr(self.bill_date, 'to_alipay_dict'):
                params['bill_date'] = self.bill_date.to_alipay_dict()
            else:
                params['bill_date'] = self.bill_date
        if self.partner_pid:
            if hasattr(self.partner_pid, 'to_alipay_dict'):
                params['partner_pid'] = self.partner_pid.to_alipay_dict()
            else:
                params['partner_pid'] = self.partner_pid
        if self.school_no:
            if hasattr(self.school_no, 'to_alipay_dict'):
                params['school_no'] = self.school_no.to_alipay_dict()
            else:
                params['school_no'] = self.school_no
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
        o = AlipayEcoEduKtSettleinfoQueryModel()
        if 'bill_date' in d:
            o.bill_date = d['bill_date']
        if 'partner_pid' in d:
            o.partner_pid = d['partner_pid']
        if 'school_no' in d:
            o.school_no = d['school_no']
        if 'smid' in d:
            o.smid = d['smid']
        return o


