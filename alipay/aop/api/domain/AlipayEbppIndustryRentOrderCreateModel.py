#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentPayBillDetail import RentPayBillDetail
from alipay.aop.api.domain.RentPayBankInfo import RentPayBankInfo
from alipay.aop.api.domain.RentPayContractInfo import RentPayContractInfo


class AlipayEbppIndustryRentOrderCreateModel(object):

    def __init__(self):
        self._accfund_center_no = None
        self._bill_detail = None
        self._biz_time_out = None
        self._cert_num = None
        self._housing_name = None
        self._housing_url = None
        self._org_city = None
        self._org_code = None
        self._out_biz_no = None
        self._redirect_url = None
        self._rent_bank_info = None
        self._rent_contract_info = None

    @property
    def accfund_center_no(self):
        return self._accfund_center_no

    @accfund_center_no.setter
    def accfund_center_no(self, value):
        self._accfund_center_no = value
    @property
    def bill_detail(self):
        return self._bill_detail

    @bill_detail.setter
    def bill_detail(self, value):
        if isinstance(value, RentPayBillDetail):
            self._bill_detail = value
        else:
            self._bill_detail = RentPayBillDetail.from_alipay_dict(value)
    @property
    def biz_time_out(self):
        return self._biz_time_out

    @biz_time_out.setter
    def biz_time_out(self, value):
        self._biz_time_out = value
    @property
    def cert_num(self):
        return self._cert_num

    @cert_num.setter
    def cert_num(self, value):
        self._cert_num = value
    @property
    def housing_name(self):
        return self._housing_name

    @housing_name.setter
    def housing_name(self, value):
        self._housing_name = value
    @property
    def housing_url(self):
        return self._housing_url

    @housing_url.setter
    def housing_url(self, value):
        self._housing_url = value
    @property
    def org_city(self):
        return self._org_city

    @org_city.setter
    def org_city(self, value):
        self._org_city = value
    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value
    @property
    def rent_bank_info(self):
        return self._rent_bank_info

    @rent_bank_info.setter
    def rent_bank_info(self, value):
        if isinstance(value, RentPayBankInfo):
            self._rent_bank_info = value
        else:
            self._rent_bank_info = RentPayBankInfo.from_alipay_dict(value)
    @property
    def rent_contract_info(self):
        return self._rent_contract_info

    @rent_contract_info.setter
    def rent_contract_info(self, value):
        if isinstance(value, RentPayContractInfo):
            self._rent_contract_info = value
        else:
            self._rent_contract_info = RentPayContractInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.accfund_center_no:
            if hasattr(self.accfund_center_no, 'to_alipay_dict'):
                params['accfund_center_no'] = self.accfund_center_no.to_alipay_dict()
            else:
                params['accfund_center_no'] = self.accfund_center_no
        if self.bill_detail:
            if hasattr(self.bill_detail, 'to_alipay_dict'):
                params['bill_detail'] = self.bill_detail.to_alipay_dict()
            else:
                params['bill_detail'] = self.bill_detail
        if self.biz_time_out:
            if hasattr(self.biz_time_out, 'to_alipay_dict'):
                params['biz_time_out'] = self.biz_time_out.to_alipay_dict()
            else:
                params['biz_time_out'] = self.biz_time_out
        if self.cert_num:
            if hasattr(self.cert_num, 'to_alipay_dict'):
                params['cert_num'] = self.cert_num.to_alipay_dict()
            else:
                params['cert_num'] = self.cert_num
        if self.housing_name:
            if hasattr(self.housing_name, 'to_alipay_dict'):
                params['housing_name'] = self.housing_name.to_alipay_dict()
            else:
                params['housing_name'] = self.housing_name
        if self.housing_url:
            if hasattr(self.housing_url, 'to_alipay_dict'):
                params['housing_url'] = self.housing_url.to_alipay_dict()
            else:
                params['housing_url'] = self.housing_url
        if self.org_city:
            if hasattr(self.org_city, 'to_alipay_dict'):
                params['org_city'] = self.org_city.to_alipay_dict()
            else:
                params['org_city'] = self.org_city
        if self.org_code:
            if hasattr(self.org_code, 'to_alipay_dict'):
                params['org_code'] = self.org_code.to_alipay_dict()
            else:
                params['org_code'] = self.org_code
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.redirect_url:
            if hasattr(self.redirect_url, 'to_alipay_dict'):
                params['redirect_url'] = self.redirect_url.to_alipay_dict()
            else:
                params['redirect_url'] = self.redirect_url
        if self.rent_bank_info:
            if hasattr(self.rent_bank_info, 'to_alipay_dict'):
                params['rent_bank_info'] = self.rent_bank_info.to_alipay_dict()
            else:
                params['rent_bank_info'] = self.rent_bank_info
        if self.rent_contract_info:
            if hasattr(self.rent_contract_info, 'to_alipay_dict'):
                params['rent_contract_info'] = self.rent_contract_info.to_alipay_dict()
            else:
                params['rent_contract_info'] = self.rent_contract_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryRentOrderCreateModel()
        if 'accfund_center_no' in d:
            o.accfund_center_no = d['accfund_center_no']
        if 'bill_detail' in d:
            o.bill_detail = d['bill_detail']
        if 'biz_time_out' in d:
            o.biz_time_out = d['biz_time_out']
        if 'cert_num' in d:
            o.cert_num = d['cert_num']
        if 'housing_name' in d:
            o.housing_name = d['housing_name']
        if 'housing_url' in d:
            o.housing_url = d['housing_url']
        if 'org_city' in d:
            o.org_city = d['org_city']
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'redirect_url' in d:
            o.redirect_url = d['redirect_url']
        if 'rent_bank_info' in d:
            o.rent_bank_info = d['rent_bank_info']
        if 'rent_contract_info' in d:
            o.rent_contract_info = d['rent_contract_info']
        return o


