#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpPatentInfo(object):

    def __init__(self):
        self._address = None
        self._agent_person = None
        self._application_day = None
        self._application_number = None
        self._fmsjmc = None
        self._international_classification = None
        self._inventor = None
        self._jmggr = None
        self._locarnofl = None
        self._notice_date = None
        self._patent_type = None
        self._pctgbsj = None
        self._pctjrgjjdr = None
        self._pctsqsj = None
        self._proposer = None
        self._published_application_day = None
        self._published_application_number = None
        self._sdggr = None
        self._sqggh = None
        self._sqggr = None
        self._summary = None
        self._yxq = None
        self._zldljg = None
        self._zlqr = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def agent_person(self):
        return self._agent_person

    @agent_person.setter
    def agent_person(self, value):
        self._agent_person = value
    @property
    def application_day(self):
        return self._application_day

    @application_day.setter
    def application_day(self, value):
        self._application_day = value
    @property
    def application_number(self):
        return self._application_number

    @application_number.setter
    def application_number(self, value):
        self._application_number = value
    @property
    def fmsjmc(self):
        return self._fmsjmc

    @fmsjmc.setter
    def fmsjmc(self, value):
        self._fmsjmc = value
    @property
    def international_classification(self):
        return self._international_classification

    @international_classification.setter
    def international_classification(self, value):
        self._international_classification = value
    @property
    def inventor(self):
        return self._inventor

    @inventor.setter
    def inventor(self, value):
        self._inventor = value
    @property
    def jmggr(self):
        return self._jmggr

    @jmggr.setter
    def jmggr(self, value):
        self._jmggr = value
    @property
    def locarnofl(self):
        return self._locarnofl

    @locarnofl.setter
    def locarnofl(self, value):
        self._locarnofl = value
    @property
    def notice_date(self):
        return self._notice_date

    @notice_date.setter
    def notice_date(self, value):
        self._notice_date = value
    @property
    def patent_type(self):
        return self._patent_type

    @patent_type.setter
    def patent_type(self, value):
        self._patent_type = value
    @property
    def pctgbsj(self):
        return self._pctgbsj

    @pctgbsj.setter
    def pctgbsj(self, value):
        self._pctgbsj = value
    @property
    def pctjrgjjdr(self):
        return self._pctjrgjjdr

    @pctjrgjjdr.setter
    def pctjrgjjdr(self, value):
        self._pctjrgjjdr = value
    @property
    def pctsqsj(self):
        return self._pctsqsj

    @pctsqsj.setter
    def pctsqsj(self, value):
        self._pctsqsj = value
    @property
    def proposer(self):
        return self._proposer

    @proposer.setter
    def proposer(self, value):
        self._proposer = value
    @property
    def published_application_day(self):
        return self._published_application_day

    @published_application_day.setter
    def published_application_day(self, value):
        self._published_application_day = value
    @property
    def published_application_number(self):
        return self._published_application_number

    @published_application_number.setter
    def published_application_number(self, value):
        self._published_application_number = value
    @property
    def sdggr(self):
        return self._sdggr

    @sdggr.setter
    def sdggr(self, value):
        self._sdggr = value
    @property
    def sqggh(self):
        return self._sqggh

    @sqggh.setter
    def sqggh(self, value):
        self._sqggh = value
    @property
    def sqggr(self):
        return self._sqggr

    @sqggr.setter
    def sqggr(self, value):
        self._sqggr = value
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        self._summary = value
    @property
    def yxq(self):
        return self._yxq

    @yxq.setter
    def yxq(self, value):
        self._yxq = value
    @property
    def zldljg(self):
        return self._zldljg

    @zldljg.setter
    def zldljg(self, value):
        self._zldljg = value
    @property
    def zlqr(self):
        return self._zlqr

    @zlqr.setter
    def zlqr(self, value):
        self._zlqr = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.agent_person:
            if hasattr(self.agent_person, 'to_alipay_dict'):
                params['agent_person'] = self.agent_person.to_alipay_dict()
            else:
                params['agent_person'] = self.agent_person
        if self.application_day:
            if hasattr(self.application_day, 'to_alipay_dict'):
                params['application_day'] = self.application_day.to_alipay_dict()
            else:
                params['application_day'] = self.application_day
        if self.application_number:
            if hasattr(self.application_number, 'to_alipay_dict'):
                params['application_number'] = self.application_number.to_alipay_dict()
            else:
                params['application_number'] = self.application_number
        if self.fmsjmc:
            if hasattr(self.fmsjmc, 'to_alipay_dict'):
                params['fmsjmc'] = self.fmsjmc.to_alipay_dict()
            else:
                params['fmsjmc'] = self.fmsjmc
        if self.international_classification:
            if hasattr(self.international_classification, 'to_alipay_dict'):
                params['international_classification'] = self.international_classification.to_alipay_dict()
            else:
                params['international_classification'] = self.international_classification
        if self.inventor:
            if hasattr(self.inventor, 'to_alipay_dict'):
                params['inventor'] = self.inventor.to_alipay_dict()
            else:
                params['inventor'] = self.inventor
        if self.jmggr:
            if hasattr(self.jmggr, 'to_alipay_dict'):
                params['jmggr'] = self.jmggr.to_alipay_dict()
            else:
                params['jmggr'] = self.jmggr
        if self.locarnofl:
            if hasattr(self.locarnofl, 'to_alipay_dict'):
                params['locarnofl'] = self.locarnofl.to_alipay_dict()
            else:
                params['locarnofl'] = self.locarnofl
        if self.notice_date:
            if hasattr(self.notice_date, 'to_alipay_dict'):
                params['notice_date'] = self.notice_date.to_alipay_dict()
            else:
                params['notice_date'] = self.notice_date
        if self.patent_type:
            if hasattr(self.patent_type, 'to_alipay_dict'):
                params['patent_type'] = self.patent_type.to_alipay_dict()
            else:
                params['patent_type'] = self.patent_type
        if self.pctgbsj:
            if hasattr(self.pctgbsj, 'to_alipay_dict'):
                params['pctgbsj'] = self.pctgbsj.to_alipay_dict()
            else:
                params['pctgbsj'] = self.pctgbsj
        if self.pctjrgjjdr:
            if hasattr(self.pctjrgjjdr, 'to_alipay_dict'):
                params['pctjrgjjdr'] = self.pctjrgjjdr.to_alipay_dict()
            else:
                params['pctjrgjjdr'] = self.pctjrgjjdr
        if self.pctsqsj:
            if hasattr(self.pctsqsj, 'to_alipay_dict'):
                params['pctsqsj'] = self.pctsqsj.to_alipay_dict()
            else:
                params['pctsqsj'] = self.pctsqsj
        if self.proposer:
            if hasattr(self.proposer, 'to_alipay_dict'):
                params['proposer'] = self.proposer.to_alipay_dict()
            else:
                params['proposer'] = self.proposer
        if self.published_application_day:
            if hasattr(self.published_application_day, 'to_alipay_dict'):
                params['published_application_day'] = self.published_application_day.to_alipay_dict()
            else:
                params['published_application_day'] = self.published_application_day
        if self.published_application_number:
            if hasattr(self.published_application_number, 'to_alipay_dict'):
                params['published_application_number'] = self.published_application_number.to_alipay_dict()
            else:
                params['published_application_number'] = self.published_application_number
        if self.sdggr:
            if hasattr(self.sdggr, 'to_alipay_dict'):
                params['sdggr'] = self.sdggr.to_alipay_dict()
            else:
                params['sdggr'] = self.sdggr
        if self.sqggh:
            if hasattr(self.sqggh, 'to_alipay_dict'):
                params['sqggh'] = self.sqggh.to_alipay_dict()
            else:
                params['sqggh'] = self.sqggh
        if self.sqggr:
            if hasattr(self.sqggr, 'to_alipay_dict'):
                params['sqggr'] = self.sqggr.to_alipay_dict()
            else:
                params['sqggr'] = self.sqggr
        if self.summary:
            if hasattr(self.summary, 'to_alipay_dict'):
                params['summary'] = self.summary.to_alipay_dict()
            else:
                params['summary'] = self.summary
        if self.yxq:
            if hasattr(self.yxq, 'to_alipay_dict'):
                params['yxq'] = self.yxq.to_alipay_dict()
            else:
                params['yxq'] = self.yxq
        if self.zldljg:
            if hasattr(self.zldljg, 'to_alipay_dict'):
                params['zldljg'] = self.zldljg.to_alipay_dict()
            else:
                params['zldljg'] = self.zldljg
        if self.zlqr:
            if hasattr(self.zlqr, 'to_alipay_dict'):
                params['zlqr'] = self.zlqr.to_alipay_dict()
            else:
                params['zlqr'] = self.zlqr
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpPatentInfo()
        if 'address' in d:
            o.address = d['address']
        if 'agent_person' in d:
            o.agent_person = d['agent_person']
        if 'application_day' in d:
            o.application_day = d['application_day']
        if 'application_number' in d:
            o.application_number = d['application_number']
        if 'fmsjmc' in d:
            o.fmsjmc = d['fmsjmc']
        if 'international_classification' in d:
            o.international_classification = d['international_classification']
        if 'inventor' in d:
            o.inventor = d['inventor']
        if 'jmggr' in d:
            o.jmggr = d['jmggr']
        if 'locarnofl' in d:
            o.locarnofl = d['locarnofl']
        if 'notice_date' in d:
            o.notice_date = d['notice_date']
        if 'patent_type' in d:
            o.patent_type = d['patent_type']
        if 'pctgbsj' in d:
            o.pctgbsj = d['pctgbsj']
        if 'pctjrgjjdr' in d:
            o.pctjrgjjdr = d['pctjrgjjdr']
        if 'pctsqsj' in d:
            o.pctsqsj = d['pctsqsj']
        if 'proposer' in d:
            o.proposer = d['proposer']
        if 'published_application_day' in d:
            o.published_application_day = d['published_application_day']
        if 'published_application_number' in d:
            o.published_application_number = d['published_application_number']
        if 'sdggr' in d:
            o.sdggr = d['sdggr']
        if 'sqggh' in d:
            o.sqggh = d['sqggh']
        if 'sqggr' in d:
            o.sqggr = d['sqggr']
        if 'summary' in d:
            o.summary = d['summary']
        if 'yxq' in d:
            o.yxq = d['yxq']
        if 'zldljg' in d:
            o.zldljg = d['zldljg']
        if 'zlqr' in d:
            o.zlqr = d['zlqr']
        return o


