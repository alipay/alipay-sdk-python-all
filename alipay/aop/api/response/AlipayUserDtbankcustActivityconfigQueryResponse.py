#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DtBankActivityTimeInfo import DtBankActivityTimeInfo
from alipay.aop.api.domain.DtBankActivityTypeInfo import DtBankActivityTypeInfo
from alipay.aop.api.domain.DtbankActivityAlertConfigInfo import DtbankActivityAlertConfigInfo
from alipay.aop.api.domain.DtBankInfo import DtBankInfo
from alipay.aop.api.domain.DtBankBudgetInfo import DtBankBudgetInfo
from alipay.aop.api.domain.DtBankCrowdInfo import DtBankCrowdInfo
from alipay.aop.api.domain.DtbankActivityDataEffectInfo import DtbankActivityDataEffectInfo
from alipay.aop.api.domain.DtBankPreferenceTypeInfo import DtBankPreferenceTypeInfo


class AlipayUserDtbankcustActivityconfigQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserDtbankcustActivityconfigQueryResponse, self).__init__()
        self._activity_id = None
        self._activity_name = None
        self._activity_status = None
        self._activity_time_info = None
        self._activity_type_info = None
        self._alert_config_info = None
        self._bank_info = None
        self._budget_info = None
        self._count_limit = None
        self._crowd_info = None
        self._data_effect_info = None
        self._preference_type_info = None
        self._use_scene = None
        self._voucher_template_id = None
        self._white_list_info = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def activity_status(self):
        return self._activity_status

    @activity_status.setter
    def activity_status(self, value):
        self._activity_status = value
    @property
    def activity_time_info(self):
        return self._activity_time_info

    @activity_time_info.setter
    def activity_time_info(self, value):
        if isinstance(value, DtBankActivityTimeInfo):
            self._activity_time_info = value
        else:
            self._activity_time_info = DtBankActivityTimeInfo.from_alipay_dict(value)
    @property
    def activity_type_info(self):
        return self._activity_type_info

    @activity_type_info.setter
    def activity_type_info(self, value):
        if isinstance(value, DtBankActivityTypeInfo):
            self._activity_type_info = value
        else:
            self._activity_type_info = DtBankActivityTypeInfo.from_alipay_dict(value)
    @property
    def alert_config_info(self):
        return self._alert_config_info

    @alert_config_info.setter
    def alert_config_info(self, value):
        if isinstance(value, DtbankActivityAlertConfigInfo):
            self._alert_config_info = value
        else:
            self._alert_config_info = DtbankActivityAlertConfigInfo.from_alipay_dict(value)
    @property
    def bank_info(self):
        return self._bank_info

    @bank_info.setter
    def bank_info(self, value):
        if isinstance(value, DtBankInfo):
            self._bank_info = value
        else:
            self._bank_info = DtBankInfo.from_alipay_dict(value)
    @property
    def budget_info(self):
        return self._budget_info

    @budget_info.setter
    def budget_info(self, value):
        if isinstance(value, DtBankBudgetInfo):
            self._budget_info = value
        else:
            self._budget_info = DtBankBudgetInfo.from_alipay_dict(value)
    @property
    def count_limit(self):
        return self._count_limit

    @count_limit.setter
    def count_limit(self, value):
        self._count_limit = value
    @property
    def crowd_info(self):
        return self._crowd_info

    @crowd_info.setter
    def crowd_info(self, value):
        if isinstance(value, DtBankCrowdInfo):
            self._crowd_info = value
        else:
            self._crowd_info = DtBankCrowdInfo.from_alipay_dict(value)
    @property
    def data_effect_info(self):
        return self._data_effect_info

    @data_effect_info.setter
    def data_effect_info(self, value):
        if isinstance(value, DtbankActivityDataEffectInfo):
            self._data_effect_info = value
        else:
            self._data_effect_info = DtbankActivityDataEffectInfo.from_alipay_dict(value)
    @property
    def preference_type_info(self):
        return self._preference_type_info

    @preference_type_info.setter
    def preference_type_info(self, value):
        if isinstance(value, DtBankPreferenceTypeInfo):
            self._preference_type_info = value
        else:
            self._preference_type_info = DtBankPreferenceTypeInfo.from_alipay_dict(value)
    @property
    def use_scene(self):
        return self._use_scene

    @use_scene.setter
    def use_scene(self, value):
        self._use_scene = value
    @property
    def voucher_template_id(self):
        return self._voucher_template_id

    @voucher_template_id.setter
    def voucher_template_id(self, value):
        self._voucher_template_id = value
    @property
    def white_list_info(self):
        return self._white_list_info

    @white_list_info.setter
    def white_list_info(self, value):
        self._white_list_info = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserDtbankcustActivityconfigQueryResponse, self).parse_response_content(response_content)
        if 'activity_id' in response:
            self.activity_id = response['activity_id']
        if 'activity_name' in response:
            self.activity_name = response['activity_name']
        if 'activity_status' in response:
            self.activity_status = response['activity_status']
        if 'activity_time_info' in response:
            self.activity_time_info = response['activity_time_info']
        if 'activity_type_info' in response:
            self.activity_type_info = response['activity_type_info']
        if 'alert_config_info' in response:
            self.alert_config_info = response['alert_config_info']
        if 'bank_info' in response:
            self.bank_info = response['bank_info']
        if 'budget_info' in response:
            self.budget_info = response['budget_info']
        if 'count_limit' in response:
            self.count_limit = response['count_limit']
        if 'crowd_info' in response:
            self.crowd_info = response['crowd_info']
        if 'data_effect_info' in response:
            self.data_effect_info = response['data_effect_info']
        if 'preference_type_info' in response:
            self.preference_type_info = response['preference_type_info']
        if 'use_scene' in response:
            self.use_scene = response['use_scene']
        if 'voucher_template_id' in response:
            self.voucher_template_id = response['voucher_template_id']
        if 'white_list_info' in response:
            self.white_list_info = response['white_list_info']
