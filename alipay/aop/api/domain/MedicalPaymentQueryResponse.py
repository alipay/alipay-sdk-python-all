#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalPaymentQueryResponse(object):

    def __init__(self):
        self._account_amount = None
        self._chnl_ord_sn = None
        self._error_reason = None
        self._gmt_out_create = None
        self._gmt_paid = None
        self._gov_amount = None
        self._insurance_subsidy_amount = None
        self._insurance_subsidy_mode = None
        self._med_org_ord = None
        self._medical_pay_status = None
        self._medical_refund_amount = None
        self._openapi_app_id = None
        self._org_no = None
        self._other_amount = None
        self._out_trade_no = None
        self._own_pay_status = None
        self._pay_order_id = None
        self._pay_type = None
        self._pid = None
        self._real_amount = None
        self._real_refund_amount = None
        self._rels_pay_flag = None
        self._rels_pay_user_name = None
        self._remark = None
        self._request_content = None
        self._total_amount = None
        self._trade_no = None

    @property
    def account_amount(self):
        return self._account_amount

    @account_amount.setter
    def account_amount(self, value):
        self._account_amount = value
    @property
    def chnl_ord_sn(self):
        return self._chnl_ord_sn

    @chnl_ord_sn.setter
    def chnl_ord_sn(self, value):
        self._chnl_ord_sn = value
    @property
    def error_reason(self):
        return self._error_reason

    @error_reason.setter
    def error_reason(self, value):
        self._error_reason = value
    @property
    def gmt_out_create(self):
        return self._gmt_out_create

    @gmt_out_create.setter
    def gmt_out_create(self, value):
        self._gmt_out_create = value
    @property
    def gmt_paid(self):
        return self._gmt_paid

    @gmt_paid.setter
    def gmt_paid(self, value):
        self._gmt_paid = value
    @property
    def gov_amount(self):
        return self._gov_amount

    @gov_amount.setter
    def gov_amount(self, value):
        self._gov_amount = value
    @property
    def insurance_subsidy_amount(self):
        return self._insurance_subsidy_amount

    @insurance_subsidy_amount.setter
    def insurance_subsidy_amount(self, value):
        self._insurance_subsidy_amount = value
    @property
    def insurance_subsidy_mode(self):
        return self._insurance_subsidy_mode

    @insurance_subsidy_mode.setter
    def insurance_subsidy_mode(self, value):
        self._insurance_subsidy_mode = value
    @property
    def med_org_ord(self):
        return self._med_org_ord

    @med_org_ord.setter
    def med_org_ord(self, value):
        self._med_org_ord = value
    @property
    def medical_pay_status(self):
        return self._medical_pay_status

    @medical_pay_status.setter
    def medical_pay_status(self, value):
        self._medical_pay_status = value
    @property
    def medical_refund_amount(self):
        return self._medical_refund_amount

    @medical_refund_amount.setter
    def medical_refund_amount(self, value):
        self._medical_refund_amount = value
    @property
    def openapi_app_id(self):
        return self._openapi_app_id

    @openapi_app_id.setter
    def openapi_app_id(self, value):
        self._openapi_app_id = value
    @property
    def org_no(self):
        return self._org_no

    @org_no.setter
    def org_no(self, value):
        self._org_no = value
    @property
    def other_amount(self):
        return self._other_amount

    @other_amount.setter
    def other_amount(self, value):
        self._other_amount = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def own_pay_status(self):
        return self._own_pay_status

    @own_pay_status.setter
    def own_pay_status(self, value):
        self._own_pay_status = value
    @property
    def pay_order_id(self):
        return self._pay_order_id

    @pay_order_id.setter
    def pay_order_id(self, value):
        self._pay_order_id = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def real_amount(self):
        return self._real_amount

    @real_amount.setter
    def real_amount(self, value):
        self._real_amount = value
    @property
    def real_refund_amount(self):
        return self._real_refund_amount

    @real_refund_amount.setter
    def real_refund_amount(self, value):
        self._real_refund_amount = value
    @property
    def rels_pay_flag(self):
        return self._rels_pay_flag

    @rels_pay_flag.setter
    def rels_pay_flag(self, value):
        self._rels_pay_flag = value
    @property
    def rels_pay_user_name(self):
        return self._rels_pay_user_name

    @rels_pay_user_name.setter
    def rels_pay_user_name(self, value):
        self._rels_pay_user_name = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def request_content(self):
        return self._request_content

    @request_content.setter
    def request_content(self, value):
        self._request_content = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_amount:
            if hasattr(self.account_amount, 'to_alipay_dict'):
                params['account_amount'] = self.account_amount.to_alipay_dict()
            else:
                params['account_amount'] = self.account_amount
        if self.chnl_ord_sn:
            if hasattr(self.chnl_ord_sn, 'to_alipay_dict'):
                params['chnl_ord_sn'] = self.chnl_ord_sn.to_alipay_dict()
            else:
                params['chnl_ord_sn'] = self.chnl_ord_sn
        if self.error_reason:
            if hasattr(self.error_reason, 'to_alipay_dict'):
                params['error_reason'] = self.error_reason.to_alipay_dict()
            else:
                params['error_reason'] = self.error_reason
        if self.gmt_out_create:
            if hasattr(self.gmt_out_create, 'to_alipay_dict'):
                params['gmt_out_create'] = self.gmt_out_create.to_alipay_dict()
            else:
                params['gmt_out_create'] = self.gmt_out_create
        if self.gmt_paid:
            if hasattr(self.gmt_paid, 'to_alipay_dict'):
                params['gmt_paid'] = self.gmt_paid.to_alipay_dict()
            else:
                params['gmt_paid'] = self.gmt_paid
        if self.gov_amount:
            if hasattr(self.gov_amount, 'to_alipay_dict'):
                params['gov_amount'] = self.gov_amount.to_alipay_dict()
            else:
                params['gov_amount'] = self.gov_amount
        if self.insurance_subsidy_amount:
            if hasattr(self.insurance_subsidy_amount, 'to_alipay_dict'):
                params['insurance_subsidy_amount'] = self.insurance_subsidy_amount.to_alipay_dict()
            else:
                params['insurance_subsidy_amount'] = self.insurance_subsidy_amount
        if self.insurance_subsidy_mode:
            if hasattr(self.insurance_subsidy_mode, 'to_alipay_dict'):
                params['insurance_subsidy_mode'] = self.insurance_subsidy_mode.to_alipay_dict()
            else:
                params['insurance_subsidy_mode'] = self.insurance_subsidy_mode
        if self.med_org_ord:
            if hasattr(self.med_org_ord, 'to_alipay_dict'):
                params['med_org_ord'] = self.med_org_ord.to_alipay_dict()
            else:
                params['med_org_ord'] = self.med_org_ord
        if self.medical_pay_status:
            if hasattr(self.medical_pay_status, 'to_alipay_dict'):
                params['medical_pay_status'] = self.medical_pay_status.to_alipay_dict()
            else:
                params['medical_pay_status'] = self.medical_pay_status
        if self.medical_refund_amount:
            if hasattr(self.medical_refund_amount, 'to_alipay_dict'):
                params['medical_refund_amount'] = self.medical_refund_amount.to_alipay_dict()
            else:
                params['medical_refund_amount'] = self.medical_refund_amount
        if self.openapi_app_id:
            if hasattr(self.openapi_app_id, 'to_alipay_dict'):
                params['openapi_app_id'] = self.openapi_app_id.to_alipay_dict()
            else:
                params['openapi_app_id'] = self.openapi_app_id
        if self.org_no:
            if hasattr(self.org_no, 'to_alipay_dict'):
                params['org_no'] = self.org_no.to_alipay_dict()
            else:
                params['org_no'] = self.org_no
        if self.other_amount:
            if hasattr(self.other_amount, 'to_alipay_dict'):
                params['other_amount'] = self.other_amount.to_alipay_dict()
            else:
                params['other_amount'] = self.other_amount
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.own_pay_status:
            if hasattr(self.own_pay_status, 'to_alipay_dict'):
                params['own_pay_status'] = self.own_pay_status.to_alipay_dict()
            else:
                params['own_pay_status'] = self.own_pay_status
        if self.pay_order_id:
            if hasattr(self.pay_order_id, 'to_alipay_dict'):
                params['pay_order_id'] = self.pay_order_id.to_alipay_dict()
            else:
                params['pay_order_id'] = self.pay_order_id
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.real_amount:
            if hasattr(self.real_amount, 'to_alipay_dict'):
                params['real_amount'] = self.real_amount.to_alipay_dict()
            else:
                params['real_amount'] = self.real_amount
        if self.real_refund_amount:
            if hasattr(self.real_refund_amount, 'to_alipay_dict'):
                params['real_refund_amount'] = self.real_refund_amount.to_alipay_dict()
            else:
                params['real_refund_amount'] = self.real_refund_amount
        if self.rels_pay_flag:
            if hasattr(self.rels_pay_flag, 'to_alipay_dict'):
                params['rels_pay_flag'] = self.rels_pay_flag.to_alipay_dict()
            else:
                params['rels_pay_flag'] = self.rels_pay_flag
        if self.rels_pay_user_name:
            if hasattr(self.rels_pay_user_name, 'to_alipay_dict'):
                params['rels_pay_user_name'] = self.rels_pay_user_name.to_alipay_dict()
            else:
                params['rels_pay_user_name'] = self.rels_pay_user_name
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.request_content:
            if hasattr(self.request_content, 'to_alipay_dict'):
                params['request_content'] = self.request_content.to_alipay_dict()
            else:
                params['request_content'] = self.request_content
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalPaymentQueryResponse()
        if 'account_amount' in d:
            o.account_amount = d['account_amount']
        if 'chnl_ord_sn' in d:
            o.chnl_ord_sn = d['chnl_ord_sn']
        if 'error_reason' in d:
            o.error_reason = d['error_reason']
        if 'gmt_out_create' in d:
            o.gmt_out_create = d['gmt_out_create']
        if 'gmt_paid' in d:
            o.gmt_paid = d['gmt_paid']
        if 'gov_amount' in d:
            o.gov_amount = d['gov_amount']
        if 'insurance_subsidy_amount' in d:
            o.insurance_subsidy_amount = d['insurance_subsidy_amount']
        if 'insurance_subsidy_mode' in d:
            o.insurance_subsidy_mode = d['insurance_subsidy_mode']
        if 'med_org_ord' in d:
            o.med_org_ord = d['med_org_ord']
        if 'medical_pay_status' in d:
            o.medical_pay_status = d['medical_pay_status']
        if 'medical_refund_amount' in d:
            o.medical_refund_amount = d['medical_refund_amount']
        if 'openapi_app_id' in d:
            o.openapi_app_id = d['openapi_app_id']
        if 'org_no' in d:
            o.org_no = d['org_no']
        if 'other_amount' in d:
            o.other_amount = d['other_amount']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'own_pay_status' in d:
            o.own_pay_status = d['own_pay_status']
        if 'pay_order_id' in d:
            o.pay_order_id = d['pay_order_id']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'pid' in d:
            o.pid = d['pid']
        if 'real_amount' in d:
            o.real_amount = d['real_amount']
        if 'real_refund_amount' in d:
            o.real_refund_amount = d['real_refund_amount']
        if 'rels_pay_flag' in d:
            o.rels_pay_flag = d['rels_pay_flag']
        if 'rels_pay_user_name' in d:
            o.rels_pay_user_name = d['rels_pay_user_name']
        if 'remark' in d:
            o.remark = d['remark']
        if 'request_content' in d:
            o.request_content = d['request_content']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


