#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserPhotoInfo import UserPhotoInfo


class AlipayOpenMiniTaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniTaskQueryResponse, self).__init__()
        self._creative_id = None
        self._creative_order_no = None
        self._fail_reason = None
        self._feeling_text = None
        self._photos = None
        self._result_image_file_url = None
        self._scene = None
        self._status = None
        self._task_id = None
        self._template_category = None
        self._template_name = None

    @property
    def creative_id(self):
        return self._creative_id

    @creative_id.setter
    def creative_id(self, value):
        self._creative_id = value
    @property
    def creative_order_no(self):
        return self._creative_order_no

    @creative_order_no.setter
    def creative_order_no(self, value):
        self._creative_order_no = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def feeling_text(self):
        return self._feeling_text

    @feeling_text.setter
    def feeling_text(self, value):
        self._feeling_text = value
    @property
    def photos(self):
        return self._photos

    @photos.setter
    def photos(self, value):
        if isinstance(value, list):
            self._photos = list()
            for i in value:
                if isinstance(i, UserPhotoInfo):
                    self._photos.append(i)
                else:
                    self._photos.append(UserPhotoInfo.from_alipay_dict(i))
    @property
    def result_image_file_url(self):
        return self._result_image_file_url

    @result_image_file_url.setter
    def result_image_file_url(self, value):
        self._result_image_file_url = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def template_category(self):
        return self._template_category

    @template_category.setter
    def template_category(self, value):
        self._template_category = value
    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, value):
        self._template_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniTaskQueryResponse, self).parse_response_content(response_content)
        if 'creative_id' in response:
            self.creative_id = response['creative_id']
        if 'creative_order_no' in response:
            self.creative_order_no = response['creative_order_no']
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'feeling_text' in response:
            self.feeling_text = response['feeling_text']
        if 'photos' in response:
            self.photos = response['photos']
        if 'result_image_file_url' in response:
            self.result_image_file_url = response['result_image_file_url']
        if 'scene' in response:
            self.scene = response['scene']
        if 'status' in response:
            self.status = response['status']
        if 'task_id' in response:
            self.task_id = response['task_id']
        if 'template_category' in response:
            self.template_category = response['template_category']
        if 'template_name' in response:
            self.template_name = response['template_name']
