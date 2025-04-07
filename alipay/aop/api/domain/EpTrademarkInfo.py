#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EpTrademarkSecondClassCodeInfo import EpTrademarkSecondClassCodeInfo


class EpTrademarkInfo(object):

    def __init__(self):
        self._address_cn = None
        self._agent = None
        self._announcement_date = None
        self._announcement_issue = None
        self._app_date = None
        self._applicant_cn = None
        self._category = None
        self._intl_cls = None
        self._jointly_owned_trademark = None
        self._logo_oss_path = None
        self._name = None
        self._private_date_end = None
        self._private_date_start = None
        self._reg_date = None
        self._reg_issue = None
        self._reg_no = None
        self._second_class_code = None
        self._status = None

    @property
    def address_cn(self):
        return self._address_cn

    @address_cn.setter
    def address_cn(self, value):
        self._address_cn = value
    @property
    def agent(self):
        return self._agent

    @agent.setter
    def agent(self, value):
        self._agent = value
    @property
    def announcement_date(self):
        return self._announcement_date

    @announcement_date.setter
    def announcement_date(self, value):
        self._announcement_date = value
    @property
    def announcement_issue(self):
        return self._announcement_issue

    @announcement_issue.setter
    def announcement_issue(self, value):
        self._announcement_issue = value
    @property
    def app_date(self):
        return self._app_date

    @app_date.setter
    def app_date(self, value):
        self._app_date = value
    @property
    def applicant_cn(self):
        return self._applicant_cn

    @applicant_cn.setter
    def applicant_cn(self, value):
        self._applicant_cn = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def intl_cls(self):
        return self._intl_cls

    @intl_cls.setter
    def intl_cls(self, value):
        self._intl_cls = value
    @property
    def jointly_owned_trademark(self):
        return self._jointly_owned_trademark

    @jointly_owned_trademark.setter
    def jointly_owned_trademark(self, value):
        self._jointly_owned_trademark = value
    @property
    def logo_oss_path(self):
        return self._logo_oss_path

    @logo_oss_path.setter
    def logo_oss_path(self, value):
        self._logo_oss_path = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def private_date_end(self):
        return self._private_date_end

    @private_date_end.setter
    def private_date_end(self, value):
        self._private_date_end = value
    @property
    def private_date_start(self):
        return self._private_date_start

    @private_date_start.setter
    def private_date_start(self, value):
        self._private_date_start = value
    @property
    def reg_date(self):
        return self._reg_date

    @reg_date.setter
    def reg_date(self, value):
        self._reg_date = value
    @property
    def reg_issue(self):
        return self._reg_issue

    @reg_issue.setter
    def reg_issue(self, value):
        self._reg_issue = value
    @property
    def reg_no(self):
        return self._reg_no

    @reg_no.setter
    def reg_no(self, value):
        self._reg_no = value
    @property
    def second_class_code(self):
        return self._second_class_code

    @second_class_code.setter
    def second_class_code(self, value):
        if isinstance(value, list):
            self._second_class_code = list()
            for i in value:
                if isinstance(i, EpTrademarkSecondClassCodeInfo):
                    self._second_class_code.append(i)
                else:
                    self._second_class_code.append(EpTrademarkSecondClassCodeInfo.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.address_cn:
            if hasattr(self.address_cn, 'to_alipay_dict'):
                params['address_cn'] = self.address_cn.to_alipay_dict()
            else:
                params['address_cn'] = self.address_cn
        if self.agent:
            if hasattr(self.agent, 'to_alipay_dict'):
                params['agent'] = self.agent.to_alipay_dict()
            else:
                params['agent'] = self.agent
        if self.announcement_date:
            if hasattr(self.announcement_date, 'to_alipay_dict'):
                params['announcement_date'] = self.announcement_date.to_alipay_dict()
            else:
                params['announcement_date'] = self.announcement_date
        if self.announcement_issue:
            if hasattr(self.announcement_issue, 'to_alipay_dict'):
                params['announcement_issue'] = self.announcement_issue.to_alipay_dict()
            else:
                params['announcement_issue'] = self.announcement_issue
        if self.app_date:
            if hasattr(self.app_date, 'to_alipay_dict'):
                params['app_date'] = self.app_date.to_alipay_dict()
            else:
                params['app_date'] = self.app_date
        if self.applicant_cn:
            if hasattr(self.applicant_cn, 'to_alipay_dict'):
                params['applicant_cn'] = self.applicant_cn.to_alipay_dict()
            else:
                params['applicant_cn'] = self.applicant_cn
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.intl_cls:
            if hasattr(self.intl_cls, 'to_alipay_dict'):
                params['intl_cls'] = self.intl_cls.to_alipay_dict()
            else:
                params['intl_cls'] = self.intl_cls
        if self.jointly_owned_trademark:
            if hasattr(self.jointly_owned_trademark, 'to_alipay_dict'):
                params['jointly_owned_trademark'] = self.jointly_owned_trademark.to_alipay_dict()
            else:
                params['jointly_owned_trademark'] = self.jointly_owned_trademark
        if self.logo_oss_path:
            if hasattr(self.logo_oss_path, 'to_alipay_dict'):
                params['logo_oss_path'] = self.logo_oss_path.to_alipay_dict()
            else:
                params['logo_oss_path'] = self.logo_oss_path
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.private_date_end:
            if hasattr(self.private_date_end, 'to_alipay_dict'):
                params['private_date_end'] = self.private_date_end.to_alipay_dict()
            else:
                params['private_date_end'] = self.private_date_end
        if self.private_date_start:
            if hasattr(self.private_date_start, 'to_alipay_dict'):
                params['private_date_start'] = self.private_date_start.to_alipay_dict()
            else:
                params['private_date_start'] = self.private_date_start
        if self.reg_date:
            if hasattr(self.reg_date, 'to_alipay_dict'):
                params['reg_date'] = self.reg_date.to_alipay_dict()
            else:
                params['reg_date'] = self.reg_date
        if self.reg_issue:
            if hasattr(self.reg_issue, 'to_alipay_dict'):
                params['reg_issue'] = self.reg_issue.to_alipay_dict()
            else:
                params['reg_issue'] = self.reg_issue
        if self.reg_no:
            if hasattr(self.reg_no, 'to_alipay_dict'):
                params['reg_no'] = self.reg_no.to_alipay_dict()
            else:
                params['reg_no'] = self.reg_no
        if self.second_class_code:
            if isinstance(self.second_class_code, list):
                for i in range(0, len(self.second_class_code)):
                    element = self.second_class_code[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.second_class_code[i] = element.to_alipay_dict()
            if hasattr(self.second_class_code, 'to_alipay_dict'):
                params['second_class_code'] = self.second_class_code.to_alipay_dict()
            else:
                params['second_class_code'] = self.second_class_code
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpTrademarkInfo()
        if 'address_cn' in d:
            o.address_cn = d['address_cn']
        if 'agent' in d:
            o.agent = d['agent']
        if 'announcement_date' in d:
            o.announcement_date = d['announcement_date']
        if 'announcement_issue' in d:
            o.announcement_issue = d['announcement_issue']
        if 'app_date' in d:
            o.app_date = d['app_date']
        if 'applicant_cn' in d:
            o.applicant_cn = d['applicant_cn']
        if 'category' in d:
            o.category = d['category']
        if 'intl_cls' in d:
            o.intl_cls = d['intl_cls']
        if 'jointly_owned_trademark' in d:
            o.jointly_owned_trademark = d['jointly_owned_trademark']
        if 'logo_oss_path' in d:
            o.logo_oss_path = d['logo_oss_path']
        if 'name' in d:
            o.name = d['name']
        if 'private_date_end' in d:
            o.private_date_end = d['private_date_end']
        if 'private_date_start' in d:
            o.private_date_start = d['private_date_start']
        if 'reg_date' in d:
            o.reg_date = d['reg_date']
        if 'reg_issue' in d:
            o.reg_issue = d['reg_issue']
        if 'reg_no' in d:
            o.reg_no = d['reg_no']
        if 'second_class_code' in d:
            o.second_class_code = d['second_class_code']
        if 'status' in d:
            o.status = d['status']
        return o


