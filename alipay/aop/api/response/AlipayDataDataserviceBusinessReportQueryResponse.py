#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BrandRankDTO import BrandRankDTO
from alipay.aop.api.domain.PortraitInMallResDTO import PortraitInMallResDTO


class AlipayDataDataserviceBusinessReportQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceBusinessReportQueryResponse, self).__init__()
        self._brand_rank_dto = None
        self._live_user_cnt_in_range_code = None
        self._portrait_in_mall_dto = None
        self._settled_user_cnt_in_range_code = None
        self._task_id = None
        self._work_user_cnt_in_range_code = None

    @property
    def brand_rank_dto(self):
        return self._brand_rank_dto

    @brand_rank_dto.setter
    def brand_rank_dto(self, value):
        if isinstance(value, BrandRankDTO):
            self._brand_rank_dto = value
        else:
            self._brand_rank_dto = BrandRankDTO.from_alipay_dict(value)
    @property
    def live_user_cnt_in_range_code(self):
        return self._live_user_cnt_in_range_code

    @live_user_cnt_in_range_code.setter
    def live_user_cnt_in_range_code(self, value):
        self._live_user_cnt_in_range_code = value
    @property
    def portrait_in_mall_dto(self):
        return self._portrait_in_mall_dto

    @portrait_in_mall_dto.setter
    def portrait_in_mall_dto(self, value):
        if isinstance(value, PortraitInMallResDTO):
            self._portrait_in_mall_dto = value
        else:
            self._portrait_in_mall_dto = PortraitInMallResDTO.from_alipay_dict(value)
    @property
    def settled_user_cnt_in_range_code(self):
        return self._settled_user_cnt_in_range_code

    @settled_user_cnt_in_range_code.setter
    def settled_user_cnt_in_range_code(self, value):
        self._settled_user_cnt_in_range_code = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def work_user_cnt_in_range_code(self):
        return self._work_user_cnt_in_range_code

    @work_user_cnt_in_range_code.setter
    def work_user_cnt_in_range_code(self, value):
        self._work_user_cnt_in_range_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceBusinessReportQueryResponse, self).parse_response_content(response_content)
        if 'brand_rank_dto' in response:
            self.brand_rank_dto = response['brand_rank_dto']
        if 'live_user_cnt_in_range_code' in response:
            self.live_user_cnt_in_range_code = response['live_user_cnt_in_range_code']
        if 'portrait_in_mall_dto' in response:
            self.portrait_in_mall_dto = response['portrait_in_mall_dto']
        if 'settled_user_cnt_in_range_code' in response:
            self.settled_user_cnt_in_range_code = response['settled_user_cnt_in_range_code']
        if 'task_id' in response:
            self.task_id = response['task_id']
        if 'work_user_cnt_in_range_code' in response:
            self.work_user_cnt_in_range_code = response['work_user_cnt_in_range_code']
