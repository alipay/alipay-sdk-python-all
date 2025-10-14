#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpNcoilopenOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNcoilopenOrderQueryResponse, self).__init__()
        self._actual_delivery_time = None
        self._apply_describe = None
        self._apply_id = None
        self._apply_time = None
        self._biz_scene_code = None
        self._biz_scene_resource_id = None
        self._download_materials_excel_url = None
        self._estimated_delivery_time = None
        self._estimated_shop_sum = None
        self._expected_delivery_time = None
        self._materials_excel_file_id = None
        self._materials_total = None
        self._production_order_no = None
        self._revoke_reason = None
        self._status = None
        self._supplier_id = None

    @property
    def actual_delivery_time(self):
        return self._actual_delivery_time

    @actual_delivery_time.setter
    def actual_delivery_time(self, value):
        self._actual_delivery_time = value
    @property
    def apply_describe(self):
        return self._apply_describe

    @apply_describe.setter
    def apply_describe(self, value):
        self._apply_describe = value
    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def biz_scene_code(self):
        return self._biz_scene_code

    @biz_scene_code.setter
    def biz_scene_code(self, value):
        self._biz_scene_code = value
    @property
    def biz_scene_resource_id(self):
        return self._biz_scene_resource_id

    @biz_scene_resource_id.setter
    def biz_scene_resource_id(self, value):
        self._biz_scene_resource_id = value
    @property
    def download_materials_excel_url(self):
        return self._download_materials_excel_url

    @download_materials_excel_url.setter
    def download_materials_excel_url(self, value):
        self._download_materials_excel_url = value
    @property
    def estimated_delivery_time(self):
        return self._estimated_delivery_time

    @estimated_delivery_time.setter
    def estimated_delivery_time(self, value):
        self._estimated_delivery_time = value
    @property
    def estimated_shop_sum(self):
        return self._estimated_shop_sum

    @estimated_shop_sum.setter
    def estimated_shop_sum(self, value):
        self._estimated_shop_sum = value
    @property
    def expected_delivery_time(self):
        return self._expected_delivery_time

    @expected_delivery_time.setter
    def expected_delivery_time(self, value):
        self._expected_delivery_time = value
    @property
    def materials_excel_file_id(self):
        return self._materials_excel_file_id

    @materials_excel_file_id.setter
    def materials_excel_file_id(self, value):
        self._materials_excel_file_id = value
    @property
    def materials_total(self):
        return self._materials_total

    @materials_total.setter
    def materials_total(self, value):
        self._materials_total = value
    @property
    def production_order_no(self):
        return self._production_order_no

    @production_order_no.setter
    def production_order_no(self, value):
        self._production_order_no = value
    @property
    def revoke_reason(self):
        return self._revoke_reason

    @revoke_reason.setter
    def revoke_reason(self, value):
        self._revoke_reason = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNcoilopenOrderQueryResponse, self).parse_response_content(response_content)
        if 'actual_delivery_time' in response:
            self.actual_delivery_time = response['actual_delivery_time']
        if 'apply_describe' in response:
            self.apply_describe = response['apply_describe']
        if 'apply_id' in response:
            self.apply_id = response['apply_id']
        if 'apply_time' in response:
            self.apply_time = response['apply_time']
        if 'biz_scene_code' in response:
            self.biz_scene_code = response['biz_scene_code']
        if 'biz_scene_resource_id' in response:
            self.biz_scene_resource_id = response['biz_scene_resource_id']
        if 'download_materials_excel_url' in response:
            self.download_materials_excel_url = response['download_materials_excel_url']
        if 'estimated_delivery_time' in response:
            self.estimated_delivery_time = response['estimated_delivery_time']
        if 'estimated_shop_sum' in response:
            self.estimated_shop_sum = response['estimated_shop_sum']
        if 'expected_delivery_time' in response:
            self.expected_delivery_time = response['expected_delivery_time']
        if 'materials_excel_file_id' in response:
            self.materials_excel_file_id = response['materials_excel_file_id']
        if 'materials_total' in response:
            self.materials_total = response['materials_total']
        if 'production_order_no' in response:
            self.production_order_no = response['production_order_no']
        if 'revoke_reason' in response:
            self.revoke_reason = response['revoke_reason']
        if 'status' in response:
            self.status = response['status']
        if 'supplier_id' in response:
            self.supplier_id = response['supplier_id']
