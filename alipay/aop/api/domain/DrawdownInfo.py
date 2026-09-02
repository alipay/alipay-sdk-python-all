#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DrawdownInfo(object):

    def __init__(self):
        self._act_repay_date = None
        self._actual_inte = None
        self._actual_intefine = None
        self._actual_overdue_corp = None
        self._actual_overdue_corp_inte = None
        self._actual_poundage_inte = None
        self._actual_service_fee = None
        self._exempt_amt = None
        self._license_no = None
        self._org_drawdown_no = None
        self._out_repayment_no = None
        self._poundage = None
        self._total_amt = None

    @property
    def act_repay_date(self):
        return self._act_repay_date

    @act_repay_date.setter
    def act_repay_date(self, value):
        self._act_repay_date = value
    @property
    def actual_inte(self):
        return self._actual_inte

    @actual_inte.setter
    def actual_inte(self, value):
        self._actual_inte = value
    @property
    def actual_intefine(self):
        return self._actual_intefine

    @actual_intefine.setter
    def actual_intefine(self, value):
        self._actual_intefine = value
    @property
    def actual_overdue_corp(self):
        return self._actual_overdue_corp

    @actual_overdue_corp.setter
    def actual_overdue_corp(self, value):
        self._actual_overdue_corp = value
    @property
    def actual_overdue_corp_inte(self):
        return self._actual_overdue_corp_inte

    @actual_overdue_corp_inte.setter
    def actual_overdue_corp_inte(self, value):
        self._actual_overdue_corp_inte = value
    @property
    def actual_poundage_inte(self):
        return self._actual_poundage_inte

    @actual_poundage_inte.setter
    def actual_poundage_inte(self, value):
        self._actual_poundage_inte = value
    @property
    def actual_service_fee(self):
        return self._actual_service_fee

    @actual_service_fee.setter
    def actual_service_fee(self, value):
        self._actual_service_fee = value
    @property
    def exempt_amt(self):
        return self._exempt_amt

    @exempt_amt.setter
    def exempt_amt(self, value):
        self._exempt_amt = value
    @property
    def license_no(self):
        return self._license_no

    @license_no.setter
    def license_no(self, value):
        self._license_no = value
    @property
    def org_drawdown_no(self):
        return self._org_drawdown_no

    @org_drawdown_no.setter
    def org_drawdown_no(self, value):
        self._org_drawdown_no = value
    @property
    def out_repayment_no(self):
        return self._out_repayment_no

    @out_repayment_no.setter
    def out_repayment_no(self, value):
        self._out_repayment_no = value
    @property
    def poundage(self):
        return self._poundage

    @poundage.setter
    def poundage(self, value):
        self._poundage = value
    @property
    def total_amt(self):
        return self._total_amt

    @total_amt.setter
    def total_amt(self, value):
        self._total_amt = value


    def to_alipay_dict(self):
        params = dict()
        if self.act_repay_date:
            if hasattr(self.act_repay_date, 'to_alipay_dict'):
                params['act_repay_date'] = self.act_repay_date.to_alipay_dict()
            else:
                params['act_repay_date'] = self.act_repay_date
        if self.actual_inte:
            if hasattr(self.actual_inte, 'to_alipay_dict'):
                params['actual_inte'] = self.actual_inte.to_alipay_dict()
            else:
                params['actual_inte'] = self.actual_inte
        if self.actual_intefine:
            if hasattr(self.actual_intefine, 'to_alipay_dict'):
                params['actual_intefine'] = self.actual_intefine.to_alipay_dict()
            else:
                params['actual_intefine'] = self.actual_intefine
        if self.actual_overdue_corp:
            if hasattr(self.actual_overdue_corp, 'to_alipay_dict'):
                params['actual_overdue_corp'] = self.actual_overdue_corp.to_alipay_dict()
            else:
                params['actual_overdue_corp'] = self.actual_overdue_corp
        if self.actual_overdue_corp_inte:
            if hasattr(self.actual_overdue_corp_inte, 'to_alipay_dict'):
                params['actual_overdue_corp_inte'] = self.actual_overdue_corp_inte.to_alipay_dict()
            else:
                params['actual_overdue_corp_inte'] = self.actual_overdue_corp_inte
        if self.actual_poundage_inte:
            if hasattr(self.actual_poundage_inte, 'to_alipay_dict'):
                params['actual_poundage_inte'] = self.actual_poundage_inte.to_alipay_dict()
            else:
                params['actual_poundage_inte'] = self.actual_poundage_inte
        if self.actual_service_fee:
            if hasattr(self.actual_service_fee, 'to_alipay_dict'):
                params['actual_service_fee'] = self.actual_service_fee.to_alipay_dict()
            else:
                params['actual_service_fee'] = self.actual_service_fee
        if self.exempt_amt:
            if hasattr(self.exempt_amt, 'to_alipay_dict'):
                params['exempt_amt'] = self.exempt_amt.to_alipay_dict()
            else:
                params['exempt_amt'] = self.exempt_amt
        if self.license_no:
            if hasattr(self.license_no, 'to_alipay_dict'):
                params['license_no'] = self.license_no.to_alipay_dict()
            else:
                params['license_no'] = self.license_no
        if self.org_drawdown_no:
            if hasattr(self.org_drawdown_no, 'to_alipay_dict'):
                params['org_drawdown_no'] = self.org_drawdown_no.to_alipay_dict()
            else:
                params['org_drawdown_no'] = self.org_drawdown_no
        if self.out_repayment_no:
            if hasattr(self.out_repayment_no, 'to_alipay_dict'):
                params['out_repayment_no'] = self.out_repayment_no.to_alipay_dict()
            else:
                params['out_repayment_no'] = self.out_repayment_no
        if self.poundage:
            if hasattr(self.poundage, 'to_alipay_dict'):
                params['poundage'] = self.poundage.to_alipay_dict()
            else:
                params['poundage'] = self.poundage
        if self.total_amt:
            if hasattr(self.total_amt, 'to_alipay_dict'):
                params['total_amt'] = self.total_amt.to_alipay_dict()
            else:
                params['total_amt'] = self.total_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DrawdownInfo()
        if 'act_repay_date' in d:
            o.act_repay_date = d['act_repay_date']
        if 'actual_inte' in d:
            o.actual_inte = d['actual_inte']
        if 'actual_intefine' in d:
            o.actual_intefine = d['actual_intefine']
        if 'actual_overdue_corp' in d:
            o.actual_overdue_corp = d['actual_overdue_corp']
        if 'actual_overdue_corp_inte' in d:
            o.actual_overdue_corp_inte = d['actual_overdue_corp_inte']
        if 'actual_poundage_inte' in d:
            o.actual_poundage_inte = d['actual_poundage_inte']
        if 'actual_service_fee' in d:
            o.actual_service_fee = d['actual_service_fee']
        if 'exempt_amt' in d:
            o.exempt_amt = d['exempt_amt']
        if 'license_no' in d:
            o.license_no = d['license_no']
        if 'org_drawdown_no' in d:
            o.org_drawdown_no = d['org_drawdown_no']
        if 'out_repayment_no' in d:
            o.out_repayment_no = d['out_repayment_no']
        if 'poundage' in d:
            o.poundage = d['poundage']
        if 'total_amt' in d:
            o.total_amt = d['total_amt']
        return o


