#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlipmcMetaqMessageOpenMqDTO import AlipmcMetaqMessageOpenMqDTO
from alipay.aop.api.domain.AlipmcProcessInstanceOpenMqDTO import AlipmcProcessInstanceOpenMqDTO
from alipay.aop.api.domain.VariablesOfProcessInstanceOpenMqDTO import VariablesOfProcessInstanceOpenMqDTO


class BpmsMessageDTO(object):

    def __init__(self):
        self._alipmc_metaq_message_open_mq_dto = None
        self._alipmc_process_instance_open_mq_dto = None
        self._platform_code = None
        self._variables_of_process_instance_open_mq_dto_list = None

    @property
    def alipmc_metaq_message_open_mq_dto(self):
        return self._alipmc_metaq_message_open_mq_dto

    @alipmc_metaq_message_open_mq_dto.setter
    def alipmc_metaq_message_open_mq_dto(self, value):
        if isinstance(value, AlipmcMetaqMessageOpenMqDTO):
            self._alipmc_metaq_message_open_mq_dto = value
        else:
            self._alipmc_metaq_message_open_mq_dto = AlipmcMetaqMessageOpenMqDTO.from_alipay_dict(value)
    @property
    def alipmc_process_instance_open_mq_dto(self):
        return self._alipmc_process_instance_open_mq_dto

    @alipmc_process_instance_open_mq_dto.setter
    def alipmc_process_instance_open_mq_dto(self, value):
        if isinstance(value, AlipmcProcessInstanceOpenMqDTO):
            self._alipmc_process_instance_open_mq_dto = value
        else:
            self._alipmc_process_instance_open_mq_dto = AlipmcProcessInstanceOpenMqDTO.from_alipay_dict(value)
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def variables_of_process_instance_open_mq_dto_list(self):
        return self._variables_of_process_instance_open_mq_dto_list

    @variables_of_process_instance_open_mq_dto_list.setter
    def variables_of_process_instance_open_mq_dto_list(self, value):
        if isinstance(value, list):
            self._variables_of_process_instance_open_mq_dto_list = list()
            for i in value:
                if isinstance(i, VariablesOfProcessInstanceOpenMqDTO):
                    self._variables_of_process_instance_open_mq_dto_list.append(i)
                else:
                    self._variables_of_process_instance_open_mq_dto_list.append(VariablesOfProcessInstanceOpenMqDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.alipmc_metaq_message_open_mq_dto:
            if hasattr(self.alipmc_metaq_message_open_mq_dto, 'to_alipay_dict'):
                params['alipmc_metaq_message_open_mq_dto'] = self.alipmc_metaq_message_open_mq_dto.to_alipay_dict()
            else:
                params['alipmc_metaq_message_open_mq_dto'] = self.alipmc_metaq_message_open_mq_dto
        if self.alipmc_process_instance_open_mq_dto:
            if hasattr(self.alipmc_process_instance_open_mq_dto, 'to_alipay_dict'):
                params['alipmc_process_instance_open_mq_dto'] = self.alipmc_process_instance_open_mq_dto.to_alipay_dict()
            else:
                params['alipmc_process_instance_open_mq_dto'] = self.alipmc_process_instance_open_mq_dto
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.variables_of_process_instance_open_mq_dto_list:
            if isinstance(self.variables_of_process_instance_open_mq_dto_list, list):
                for i in range(0, len(self.variables_of_process_instance_open_mq_dto_list)):
                    element = self.variables_of_process_instance_open_mq_dto_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.variables_of_process_instance_open_mq_dto_list[i] = element.to_alipay_dict()
            if hasattr(self.variables_of_process_instance_open_mq_dto_list, 'to_alipay_dict'):
                params['variables_of_process_instance_open_mq_dto_list'] = self.variables_of_process_instance_open_mq_dto_list.to_alipay_dict()
            else:
                params['variables_of_process_instance_open_mq_dto_list'] = self.variables_of_process_instance_open_mq_dto_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BpmsMessageDTO()
        if 'alipmc_metaq_message_open_mq_dto' in d:
            o.alipmc_metaq_message_open_mq_dto = d['alipmc_metaq_message_open_mq_dto']
        if 'alipmc_process_instance_open_mq_dto' in d:
            o.alipmc_process_instance_open_mq_dto = d['alipmc_process_instance_open_mq_dto']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'variables_of_process_instance_open_mq_dto_list' in d:
            o.variables_of_process_instance_open_mq_dto_list = d['variables_of_process_instance_open_mq_dto_list']
        return o


