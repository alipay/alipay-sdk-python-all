#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.YXTAttachmentDTO import YXTAttachmentDTO


class AlipayDigitalmgmtEmbenefitCoursetreeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtEmbenefitCoursetreeQueryResponse, self).__init__()
        self._attachments = None
        self._course_id = None
        self._course_name = None
        self._image = None
        self._status = None
        self._tenant_id = None
        self._total_video_count = None

    @property
    def attachments(self):
        return self._attachments

    @attachments.setter
    def attachments(self, value):
        if isinstance(value, list):
            self._attachments = list()
            for i in value:
                if isinstance(i, YXTAttachmentDTO):
                    self._attachments.append(i)
                else:
                    self._attachments.append(YXTAttachmentDTO.from_alipay_dict(i))
    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        self._course_id = value
    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, value):
        self._course_name = value
    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value
    @property
    def total_video_count(self):
        return self._total_video_count

    @total_video_count.setter
    def total_video_count(self, value):
        self._total_video_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtEmbenefitCoursetreeQueryResponse, self).parse_response_content(response_content)
        if 'attachments' in response:
            self.attachments = response['attachments']
        if 'course_id' in response:
            self.course_id = response['course_id']
        if 'course_name' in response:
            self.course_name = response['course_name']
        if 'image' in response:
            self.image = response['image']
        if 'status' in response:
            self.status = response['status']
        if 'tenant_id' in response:
            self.tenant_id = response['tenant_id']
        if 'total_video_count' in response:
            self.total_video_count = response['total_video_count']
