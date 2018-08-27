#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsAddressee import InsAddressee
from alipay.aop.api.domain.InsPerson import InsPerson
from alipay.aop.api.domain.InsClaim import InsClaim
from alipay.aop.api.domain.InsCoverage import InsCoverage
from alipay.aop.api.domain.InsObject import InsObject
from alipay.aop.api.domain.InsPerson import InsPerson


class InsPolicy(object):

    def __init__(self):
        self._addressee = None
        self._applicant = None
        self._biz_data = None
        self._claims = None
        self._coverages = None
        self._effect_end_time = None
        self._effect_start_time = None
        self._ins_objects = None
        self._insureds = None
        self._merchant_name = None
        self._out_policy_no = None
        self._pay_end_time = None
        self._pay_to_time = None
        self._policy_no = None
        self._policy_status = None
        self._premium = None
        self._prod_name = None
        self._sum_insured = None
        self._surrender_fee = None
        self._surrender_time = None

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
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def claims(self):
        return self._claims

    @claims.setter
    def claims(self, value):
        if isinstance(value, list):
            self._claims = list()
            for i in value:
                if isinstance(i, InsClaim):
                    self._claims.append(i)
                else:
                    self._claims.append(InsClaim.from_alipay_dict(i))
    @property
    def coverages(self):
        return self._coverages

    @coverages.setter
    def coverages(self, value):
        if isinstance(value, list):
            self._coverages = list()
            for i in value:
                if isinstance(i, InsCoverage):
                    self._coverages.append(i)
                else:
                    self._coverages.append(InsCoverage.from_alipay_dict(i))
    @property
    def effect_end_time(self):
        return self._effect_end_time

    @effect_end_time.setter
    def effect_end_time(self, value):
        self._effect_end_time = value
    @property
    def effect_start_time(self):
        return self._effect_start_time

    @effect_start_time.setter
    def effect_start_time(self, value):
        self._effect_start_time = value
    @property
    def ins_objects(self):
        return self._ins_objects

    @ins_objects.setter
    def ins_objects(self, value):
        if isinstance(value, list):
            self._ins_objects = list()
            for i in value:
                if isinstance(i, InsObject):
                    self._ins_objects.append(i)
                else:
                    self._ins_objects.append(InsObject.from_alipay_dict(i))
    @property
    def insureds(self):
        return self._insureds

    @insureds.setter
    def insureds(self, value):
        if isinstance(value, list):
            self._insureds = list()
            for i in value:
                if isinstance(i, InsPerson):
                    self._insureds.append(i)
                else:
                    self._insureds.append(InsPerson.from_alipay_dict(i))
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def out_policy_no(self):
        return self._out_policy_no

    @out_policy_no.setter
    def out_policy_no(self, value):
        self._out_policy_no = value
    @property
    def pay_end_time(self):
        return self._pay_end_time

    @pay_end_time.setter
    def pay_end_time(self, value):
        self._pay_end_time = value
    @property
    def pay_to_time(self):
        return self._pay_to_time

    @pay_to_time.setter
    def pay_to_time(self, value):
        self._pay_to_time = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def policy_status(self):
        return self._policy_status

    @policy_status.setter
    def policy_status(self, value):
        self._policy_status = value
    @property
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, value):
        self._premium = value
    @property
    def prod_name(self):
        return self._prod_name

    @prod_name.setter
    def prod_name(self, value):
        self._prod_name = value
    @property
    def sum_insured(self):
        return self._sum_insured

    @sum_insured.setter
    def sum_insured(self, value):
        self._sum_insured = value
    @property
    def surrender_fee(self):
        return self._surrender_fee

    @surrender_fee.setter
    def surrender_fee(self, value):
        self._surrender_fee = value
    @property
    def surrender_time(self):
        return self._surrender_time

    @surrender_time.setter
    def surrender_time(self, value):
        self._surrender_time = value


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
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.claims:
            if isinstance(self.claims, list):
                for i in range(0, len(self.claims)):
                    element = self.claims[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.claims[i] = element.to_alipay_dict()
            if hasattr(self.claims, 'to_alipay_dict'):
                params['claims'] = self.claims.to_alipay_dict()
            else:
                params['claims'] = self.claims
        if self.coverages:
            if isinstance(self.coverages, list):
                for i in range(0, len(self.coverages)):
                    element = self.coverages[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.coverages[i] = element.to_alipay_dict()
            if hasattr(self.coverages, 'to_alipay_dict'):
                params['coverages'] = self.coverages.to_alipay_dict()
            else:
                params['coverages'] = self.coverages
        if self.effect_end_time:
            if hasattr(self.effect_end_time, 'to_alipay_dict'):
                params['effect_end_time'] = self.effect_end_time.to_alipay_dict()
            else:
                params['effect_end_time'] = self.effect_end_time
        if self.effect_start_time:
            if hasattr(self.effect_start_time, 'to_alipay_dict'):
                params['effect_start_time'] = self.effect_start_time.to_alipay_dict()
            else:
                params['effect_start_time'] = self.effect_start_time
        if self.ins_objects:
            if isinstance(self.ins_objects, list):
                for i in range(0, len(self.ins_objects)):
                    element = self.ins_objects[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ins_objects[i] = element.to_alipay_dict()
            if hasattr(self.ins_objects, 'to_alipay_dict'):
                params['ins_objects'] = self.ins_objects.to_alipay_dict()
            else:
                params['ins_objects'] = self.ins_objects
        if self.insureds:
            if isinstance(self.insureds, list):
                for i in range(0, len(self.insureds)):
                    element = self.insureds[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.insureds[i] = element.to_alipay_dict()
            if hasattr(self.insureds, 'to_alipay_dict'):
                params['insureds'] = self.insureds.to_alipay_dict()
            else:
                params['insureds'] = self.insureds
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.out_policy_no:
            if hasattr(self.out_policy_no, 'to_alipay_dict'):
                params['out_policy_no'] = self.out_policy_no.to_alipay_dict()
            else:
                params['out_policy_no'] = self.out_policy_no
        if self.pay_end_time:
            if hasattr(self.pay_end_time, 'to_alipay_dict'):
                params['pay_end_time'] = self.pay_end_time.to_alipay_dict()
            else:
                params['pay_end_time'] = self.pay_end_time
        if self.pay_to_time:
            if hasattr(self.pay_to_time, 'to_alipay_dict'):
                params['pay_to_time'] = self.pay_to_time.to_alipay_dict()
            else:
                params['pay_to_time'] = self.pay_to_time
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        if self.policy_status:
            if hasattr(self.policy_status, 'to_alipay_dict'):
                params['policy_status'] = self.policy_status.to_alipay_dict()
            else:
                params['policy_status'] = self.policy_status
        if self.premium:
            if hasattr(self.premium, 'to_alipay_dict'):
                params['premium'] = self.premium.to_alipay_dict()
            else:
                params['premium'] = self.premium
        if self.prod_name:
            if hasattr(self.prod_name, 'to_alipay_dict'):
                params['prod_name'] = self.prod_name.to_alipay_dict()
            else:
                params['prod_name'] = self.prod_name
        if self.sum_insured:
            if hasattr(self.sum_insured, 'to_alipay_dict'):
                params['sum_insured'] = self.sum_insured.to_alipay_dict()
            else:
                params['sum_insured'] = self.sum_insured
        if self.surrender_fee:
            if hasattr(self.surrender_fee, 'to_alipay_dict'):
                params['surrender_fee'] = self.surrender_fee.to_alipay_dict()
            else:
                params['surrender_fee'] = self.surrender_fee
        if self.surrender_time:
            if hasattr(self.surrender_time, 'to_alipay_dict'):
                params['surrender_time'] = self.surrender_time.to_alipay_dict()
            else:
                params['surrender_time'] = self.surrender_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsPolicy()
        if 'addressee' in d:
            o.addressee = d['addressee']
        if 'applicant' in d:
            o.applicant = d['applicant']
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'claims' in d:
            o.claims = d['claims']
        if 'coverages' in d:
            o.coverages = d['coverages']
        if 'effect_end_time' in d:
            o.effect_end_time = d['effect_end_time']
        if 'effect_start_time' in d:
            o.effect_start_time = d['effect_start_time']
        if 'ins_objects' in d:
            o.ins_objects = d['ins_objects']
        if 'insureds' in d:
            o.insureds = d['insureds']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'out_policy_no' in d:
            o.out_policy_no = d['out_policy_no']
        if 'pay_end_time' in d:
            o.pay_end_time = d['pay_end_time']
        if 'pay_to_time' in d:
            o.pay_to_time = d['pay_to_time']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'policy_status' in d:
            o.policy_status = d['policy_status']
        if 'premium' in d:
            o.premium = d['premium']
        if 'prod_name' in d:
            o.prod_name = d['prod_name']
        if 'sum_insured' in d:
            o.sum_insured = d['sum_insured']
        if 'surrender_fee' in d:
            o.surrender_fee = d['surrender_fee']
        if 'surrender_time' in d:
            o.surrender_time = d['surrender_time']
        return o


