#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCsfuCaseSyncModel(object):

    def __init__(self):
        self._biz_case_no = None
        self._case_overdue_date = None
        self._case_plans = None
        self._commission_end_time = None
        self._commission_start_time = None
        self._contact_name = None
        self._ext_info = None
        self._external_contact_id = None
        self._id_card_no = None
        self._mobile_phone = None
        self._tenant_id = None
        self._user_type = None

    @property
    def biz_case_no(self):
        return self._biz_case_no

    @biz_case_no.setter
    def biz_case_no(self, value):
        self._biz_case_no = value
    @property
    def case_overdue_date(self):
        return self._case_overdue_date

    @case_overdue_date.setter
    def case_overdue_date(self, value):
        self._case_overdue_date = value
    @property
    def case_plans(self):
        return self._case_plans

    @case_plans.setter
    def case_plans(self, value):
        if isinstance(value, list):
            self._case_plans = list()
            for i in value:
                self._case_plans.append(i)
    @property
    def commission_end_time(self):
        return self._commission_end_time

    @commission_end_time.setter
    def commission_end_time(self, value):
        self._commission_end_time = value
    @property
    def commission_start_time(self):
        return self._commission_start_time

    @commission_start_time.setter
    def commission_start_time(self, value):
        self._commission_start_time = value
    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def external_contact_id(self):
        return self._external_contact_id

    @external_contact_id.setter
    def external_contact_id(self, value):
        self._external_contact_id = value
    @property
    def id_card_no(self):
        return self._id_card_no

    @id_card_no.setter
    def id_card_no(self, value):
        self._id_card_no = value
    @property
    def mobile_phone(self):
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, value):
        self._mobile_phone = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_case_no:
            if hasattr(self.biz_case_no, 'to_alipay_dict'):
                params['biz_case_no'] = self.biz_case_no.to_alipay_dict()
            else:
                params['biz_case_no'] = self.biz_case_no
        if self.case_overdue_date:
            if hasattr(self.case_overdue_date, 'to_alipay_dict'):
                params['case_overdue_date'] = self.case_overdue_date.to_alipay_dict()
            else:
                params['case_overdue_date'] = self.case_overdue_date
        if self.case_plans:
            if isinstance(self.case_plans, list):
                for i in range(0, len(self.case_plans)):
                    element = self.case_plans[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.case_plans[i] = element.to_alipay_dict()
            if hasattr(self.case_plans, 'to_alipay_dict'):
                params['case_plans'] = self.case_plans.to_alipay_dict()
            else:
                params['case_plans'] = self.case_plans
        if self.commission_end_time:
            if hasattr(self.commission_end_time, 'to_alipay_dict'):
                params['commission_end_time'] = self.commission_end_time.to_alipay_dict()
            else:
                params['commission_end_time'] = self.commission_end_time
        if self.commission_start_time:
            if hasattr(self.commission_start_time, 'to_alipay_dict'):
                params['commission_start_time'] = self.commission_start_time.to_alipay_dict()
            else:
                params['commission_start_time'] = self.commission_start_time
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.external_contact_id:
            if hasattr(self.external_contact_id, 'to_alipay_dict'):
                params['external_contact_id'] = self.external_contact_id.to_alipay_dict()
            else:
                params['external_contact_id'] = self.external_contact_id
        if self.id_card_no:
            if hasattr(self.id_card_no, 'to_alipay_dict'):
                params['id_card_no'] = self.id_card_no.to_alipay_dict()
            else:
                params['id_card_no'] = self.id_card_no
        if self.mobile_phone:
            if hasattr(self.mobile_phone, 'to_alipay_dict'):
                params['mobile_phone'] = self.mobile_phone.to_alipay_dict()
            else:
                params['mobile_phone'] = self.mobile_phone
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        if self.user_type:
            if hasattr(self.user_type, 'to_alipay_dict'):
                params['user_type'] = self.user_type.to_alipay_dict()
            else:
                params['user_type'] = self.user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCsfuCaseSyncModel()
        if 'biz_case_no' in d:
            o.biz_case_no = d['biz_case_no']
        if 'case_overdue_date' in d:
            o.case_overdue_date = d['case_overdue_date']
        if 'case_plans' in d:
            o.case_plans = d['case_plans']
        if 'commission_end_time' in d:
            o.commission_end_time = d['commission_end_time']
        if 'commission_start_time' in d:
            o.commission_start_time = d['commission_start_time']
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'external_contact_id' in d:
            o.external_contact_id = d['external_contact_id']
        if 'id_card_no' in d:
            o.id_card_no = d['id_card_no']
        if 'mobile_phone' in d:
            o.mobile_phone = d['mobile_phone']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        if 'user_type' in d:
            o.user_type = d['user_type']
        return o


