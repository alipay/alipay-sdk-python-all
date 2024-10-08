#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SupervisorTaskInstanceDTO import SupervisorTaskInstanceDTO
from alipay.aop.api.domain.VisitShopDTO import VisitShopDTO
from alipay.aop.api.domain.VisitShopDTO import VisitShopDTO


class AlipayCommerceYuntaskSupervisortaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceYuntaskSupervisortaskQueryResponse, self).__init__()
        self._task_instance_info = None
        self._unvisit_shop_list = None
        self._visit_shop_list = None

    @property
    def task_instance_info(self):
        return self._task_instance_info

    @task_instance_info.setter
    def task_instance_info(self, value):
        if isinstance(value, SupervisorTaskInstanceDTO):
            self._task_instance_info = value
        else:
            self._task_instance_info = SupervisorTaskInstanceDTO.from_alipay_dict(value)
    @property
    def unvisit_shop_list(self):
        return self._unvisit_shop_list

    @unvisit_shop_list.setter
    def unvisit_shop_list(self, value):
        if isinstance(value, list):
            self._unvisit_shop_list = list()
            for i in value:
                if isinstance(i, VisitShopDTO):
                    self._unvisit_shop_list.append(i)
                else:
                    self._unvisit_shop_list.append(VisitShopDTO.from_alipay_dict(i))
    @property
    def visit_shop_list(self):
        return self._visit_shop_list

    @visit_shop_list.setter
    def visit_shop_list(self, value):
        if isinstance(value, list):
            self._visit_shop_list = list()
            for i in value:
                if isinstance(i, VisitShopDTO):
                    self._visit_shop_list.append(i)
                else:
                    self._visit_shop_list.append(VisitShopDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceYuntaskSupervisortaskQueryResponse, self).parse_response_content(response_content)
        if 'task_instance_info' in response:
            self.task_instance_info = response['task_instance_info']
        if 'unvisit_shop_list' in response:
            self.unvisit_shop_list = response['unvisit_shop_list']
        if 'visit_shop_list' in response:
            self.visit_shop_list = response['visit_shop_list']
