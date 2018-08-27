#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsAddressee import InsAddressee
from alipay.aop.api.domain.InsPerson import InsPerson
from alipay.aop.api.domain.InsApplication import InsApplication
from alipay.aop.api.domain.InsCoupon import InsCoupon


class AlipayInsSceneApplicationGroupApplyModel(object):

    def __init__(self):
        self._addressee = None
        self._applicant = None
        self._applications = None
        self._bill_title = None
        self._coupons = None
        self._discount_id = None
        self._out_biz_no = None
        self._prod_code = None
        self._quote_biz_id = None
        self._source = None

    @property
    def addressee(self):
        return self._addressee

    @addressee.setter
    def addressee(self, value):
        if isinstance(value, InsAddressee):
            self._addressee = value
        else:
            self._addressee = InsAddressee.from_alipay_dict(value)
    @property
    def applicant(self):
        return self._applicant

    @applicant.setter
    def applicant(self, value):
        if isinstance(value, InsPerson):
            self._applicant = value
        else:
            self._applicant = InsPerson.from_alipay_dict(value)
    @property
    def applications(self):
        return self._applications

    @applications.setter
    def applications(self, value):
        if isinstance(value, list):
            self._applications = list()
            for i in value:
                if isinstance(i, InsApplication):
                    self._applications.append(i)
                else:
                    self._applications.append(InsApplication.from_alipay_dict(i))
    @property
    def bill_title(self):
        return self._bill_title

    @bill_title.setter
    def bill_title(self, value):
        self._bill_title = value
    @property
    def coupons(self):
        return self._coupons

    @coupons.setter
    def coupons(self, value):
        if isinstance(value, list):
            self._coupons = list()
            for i in value:
                if isinstance(i, InsCoupon):
                    self._coupons.append(i)
                else:
                    self._coupons.append(InsCoupon.from_alipay_dict(i))
    @property
    def discount_id(self):
        return self._discount_id

    @discount_id.setter
    def discount_id(self, value):
        self._discount_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value
    @property
    def quote_biz_id(self):
        return self._quote_biz_id

    @quote_biz_id.setter
    def quote_biz_id(self, value):
        self._quote_biz_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.addressee:
            if hasattr(self.addressee, 'to_alipay_dict'):
                params['addressee'] = self.addressee.to_alipay_dict()
            else:
                params['addressee'] = self.addressee
        if self.applicant:
            if hasattr(self.applicant, 'to_alipay_dict'):
                params['applicant'] = self.applicant.to_alipay_dict()
            else:
                params['applicant'] = self.applicant
        if self.applications:
            if isinstance(self.applications, list):
                for i in range(0, len(self.applications)):
                    element = self.applications[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.applications[i] = element.to_alipay_dict()
            if hasattr(self.applications, 'to_alipay_dict'):
                params['applications'] = self.applications.to_alipay_dict()
            else:
                params['applications'] = self.applications
        if self.bill_title:
            if hasattr(self.bill_title, 'to_alipay_dict'):
                params['bill_title'] = self.bill_title.to_alipay_dict()
            else:
                params['bill_title'] = self.bill_title
        if self.coupons:
            if isinstance(self.coupons, list):
                for i in range(0, len(self.coupons)):
                    element = self.coupons[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.coupons[i] = element.to_alipay_dict()
            if hasattr(self.coupons, 'to_alipay_dict'):
                params['coupons'] = self.coupons.to_alipay_dict()
            else:
                params['coupons'] = self.coupons
        if self.discount_id:
            if hasattr(self.discount_id, 'to_alipay_dict'):
                params['discount_id'] = self.discount_id.to_alipay_dict()
            else:
                params['discount_id'] = self.discount_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        if self.quote_biz_id:
            if hasattr(self.quote_biz_id, 'to_alipay_dict'):
                params['quote_biz_id'] = self.quote_biz_id.to_alipay_dict()
            else:
                params['quote_biz_id'] = self.quote_biz_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneApplicationGroupApplyModel()
        if 'addressee' in d:
            o.addressee = d['addressee']
        if 'applicant' in d:
            o.applicant = d['applicant']
        if 'applications' in d:
            o.applications = d['applications']
        if 'bill_title' in d:
            o.bill_title = d['bill_title']
        if 'coupons' in d:
            o.coupons = d['coupons']
        if 'discount_id' in d:
            o.discount_id = d['discount_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        if 'quote_biz_id' in d:
            o.quote_biz_id = d['quote_biz_id']
        if 'source' in d:
            o.source = d['source']
        return o


