#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsPerson import InsPerson
from alipay.aop.api.domain.InsObject import InsObject
from alipay.aop.api.domain.InsPerson import InsPerson
from alipay.aop.api.domain.InsPerson import InsPerson


class AlipayInsSceneApplicationApplyModel(object):

    def __init__(self):
        self._activity_id = None
        self._applicant = None
        self._bill_title = None
        self._biz_data = None
        self._csu_no = None
        self._effect_start_time = None
        self._ins_objects = None
        self._insureds = None
        self._out_biz_no = None
        self._period = None
        self._premium = None
        self._prod_code = None
        self._recom_flow_no = None
        self._source = None
        self._stake_holders = None
        self._sum_insured = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
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
    def bill_title(self):
        return self._bill_title

    @bill_title.setter
    def bill_title(self, value):
        self._bill_title = value
    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def csu_no(self):
        return self._csu_no

    @csu_no.setter
    def csu_no(self, value):
        self._csu_no = value
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
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, value):
        self._premium = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value
    @property
    def recom_flow_no(self):
        return self._recom_flow_no

    @recom_flow_no.setter
    def recom_flow_no(self, value):
        self._recom_flow_no = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def stake_holders(self):
        return self._stake_holders

    @stake_holders.setter
    def stake_holders(self, value):
        if isinstance(value, list):
            self._stake_holders = list()
            for i in value:
                if isinstance(i, InsPerson):
                    self._stake_holders.append(i)
                else:
                    self._stake_holders.append(InsPerson.from_alipay_dict(i))
    @property
    def sum_insured(self):
        return self._sum_insured

    @sum_insured.setter
    def sum_insured(self, value):
        self._sum_insured = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.applicant:
            if hasattr(self.applicant, 'to_alipay_dict'):
                params['applicant'] = self.applicant.to_alipay_dict()
            else:
                params['applicant'] = self.applicant
        if self.bill_title:
            if hasattr(self.bill_title, 'to_alipay_dict'):
                params['bill_title'] = self.bill_title.to_alipay_dict()
            else:
                params['bill_title'] = self.bill_title
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.csu_no:
            if hasattr(self.csu_no, 'to_alipay_dict'):
                params['csu_no'] = self.csu_no.to_alipay_dict()
            else:
                params['csu_no'] = self.csu_no
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
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.premium:
            if hasattr(self.premium, 'to_alipay_dict'):
                params['premium'] = self.premium.to_alipay_dict()
            else:
                params['premium'] = self.premium
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        if self.recom_flow_no:
            if hasattr(self.recom_flow_no, 'to_alipay_dict'):
                params['recom_flow_no'] = self.recom_flow_no.to_alipay_dict()
            else:
                params['recom_flow_no'] = self.recom_flow_no
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.stake_holders:
            if isinstance(self.stake_holders, list):
                for i in range(0, len(self.stake_holders)):
                    element = self.stake_holders[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.stake_holders[i] = element.to_alipay_dict()
            if hasattr(self.stake_holders, 'to_alipay_dict'):
                params['stake_holders'] = self.stake_holders.to_alipay_dict()
            else:
                params['stake_holders'] = self.stake_holders
        if self.sum_insured:
            if hasattr(self.sum_insured, 'to_alipay_dict'):
                params['sum_insured'] = self.sum_insured.to_alipay_dict()
            else:
                params['sum_insured'] = self.sum_insured
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneApplicationApplyModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'applicant' in d:
            o.applicant = d['applicant']
        if 'bill_title' in d:
            o.bill_title = d['bill_title']
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'csu_no' in d:
            o.csu_no = d['csu_no']
        if 'effect_start_time' in d:
            o.effect_start_time = d['effect_start_time']
        if 'ins_objects' in d:
            o.ins_objects = d['ins_objects']
        if 'insureds' in d:
            o.insureds = d['insureds']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'period' in d:
            o.period = d['period']
        if 'premium' in d:
            o.premium = d['premium']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        if 'recom_flow_no' in d:
            o.recom_flow_no = d['recom_flow_no']
        if 'source' in d:
            o.source = d['source']
        if 'stake_holders' in d:
            o.stake_holders = d['stake_holders']
        if 'sum_insured' in d:
            o.sum_insured = d['sum_insured']
        return o


