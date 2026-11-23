#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicalRegisterButtonInfo import MedicalRegisterButtonInfo
from alipay.aop.api.domain.TreatTips import TreatTips


class MedicalRegisterOrderInfo(object):

    def __init__(self):
        self._address = None
        self._agent_id = None
        self._buss_type = None
        self._button_list = None
        self._campus_name = None
        self._cancel_reason = None
        self._cancel_time = None
        self._channel = None
        self._create_time = None
        self._date = None
        self._department_id = None
        self._department_name = None
        self._disease_description = None
        self._disease_image_item_list = None
        self._disease_name = None
        self._doctor_id = None
        self._doctor_inner_id = None
        self._doctor_logo = None
        self._doctor_name = None
        self._doctor_title = None
        self._ext_info = None
        self._first_visit_with_doctor = None
        self._hint_message = None
        self._hos_institution_code = None
        self._hospital_grade = None
        self._hospital_id = None
        self._hospital_logo = None
        self._hospital_name = None
        self._hospital_tel_number = None
        self._hospital_uniq_code = None
        self._isv_code = None
        self._isv_display_first_page_url = None
        self._isv_display_logo = None
        self._isv_display_name = None
        self._isv_name = None
        self._jump_url = None
        self._main_open_id = None
        self._main_user_id = None
        self._new_order_status = None
        self._new_order_status_desc = None
        self._number_seq_no = None
        self._order_detail_url = None
        self._order_id = None
        self._order_status = None
        self._out_order_id = None
        self._patient_id = None
        self._patient_name = None
        self._pay_type = None
        self._period = None
        self._pickup_end_time = None
        self._platform_code = None
        self._register_date = None
        self._register_evaluate = None
        self._register_fee = None
        self._register_hint_msg = None
        self._register_hos_detail_loc = None
        self._register_line_number = None
        self._register_ticket = None
        self._register_time = None
        self._register_type = None
        self._register_type_desc = None
        self._reimburse_claim_status = None
        self._reimburse_text = None
        self._reimburse_url = None
        self._scene_code = None
        self._scm_info = None
        self._status_reason = None
        self._support_refund = None
        self._tags = None
        self._treat_tips = None
        self._unit = None
        self._univ_department_id = None
        self._update_time = None
        self._visit_purpose = None
        self._week_num = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def buss_type(self):
        return self._buss_type

    @buss_type.setter
    def buss_type(self, value):
        self._buss_type = value
    @property
    def button_list(self):
        return self._button_list

    @button_list.setter
    def button_list(self, value):
        if isinstance(value, list):
            self._button_list = list()
            for i in value:
                if isinstance(i, MedicalRegisterButtonInfo):
                    self._button_list.append(i)
                else:
                    self._button_list.append(MedicalRegisterButtonInfo.from_alipay_dict(i))
    @property
    def campus_name(self):
        return self._campus_name

    @campus_name.setter
    def campus_name(self, value):
        self._campus_name = value
    @property
    def cancel_reason(self):
        return self._cancel_reason

    @cancel_reason.setter
    def cancel_reason(self, value):
        self._cancel_reason = value
    @property
    def cancel_time(self):
        return self._cancel_time

    @cancel_time.setter
    def cancel_time(self, value):
        self._cancel_time = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def department_id(self):
        return self._department_id

    @department_id.setter
    def department_id(self, value):
        self._department_id = value
    @property
    def department_name(self):
        return self._department_name

    @department_name.setter
    def department_name(self, value):
        self._department_name = value
    @property
    def disease_description(self):
        return self._disease_description

    @disease_description.setter
    def disease_description(self, value):
        self._disease_description = value
    @property
    def disease_image_item_list(self):
        return self._disease_image_item_list

    @disease_image_item_list.setter
    def disease_image_item_list(self, value):
        if isinstance(value, list):
            self._disease_image_item_list = list()
            for i in value:
                self._disease_image_item_list.append(i)
    @property
    def disease_name(self):
        return self._disease_name

    @disease_name.setter
    def disease_name(self, value):
        self._disease_name = value
    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
    @property
    def doctor_inner_id(self):
        return self._doctor_inner_id

    @doctor_inner_id.setter
    def doctor_inner_id(self, value):
        self._doctor_inner_id = value
    @property
    def doctor_logo(self):
        return self._doctor_logo

    @doctor_logo.setter
    def doctor_logo(self, value):
        self._doctor_logo = value
    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self._doctor_name = value
    @property
    def doctor_title(self):
        return self._doctor_title

    @doctor_title.setter
    def doctor_title(self, value):
        self._doctor_title = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def first_visit_with_doctor(self):
        return self._first_visit_with_doctor

    @first_visit_with_doctor.setter
    def first_visit_with_doctor(self, value):
        self._first_visit_with_doctor = value
    @property
    def hint_message(self):
        return self._hint_message

    @hint_message.setter
    def hint_message(self, value):
        self._hint_message = value
    @property
    def hos_institution_code(self):
        return self._hos_institution_code

    @hos_institution_code.setter
    def hos_institution_code(self, value):
        self._hos_institution_code = value
    @property
    def hospital_grade(self):
        return self._hospital_grade

    @hospital_grade.setter
    def hospital_grade(self, value):
        self._hospital_grade = value
    @property
    def hospital_id(self):
        return self._hospital_id

    @hospital_id.setter
    def hospital_id(self, value):
        self._hospital_id = value
    @property
    def hospital_logo(self):
        return self._hospital_logo

    @hospital_logo.setter
    def hospital_logo(self, value):
        self._hospital_logo = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def hospital_tel_number(self):
        return self._hospital_tel_number

    @hospital_tel_number.setter
    def hospital_tel_number(self, value):
        self._hospital_tel_number = value
    @property
    def hospital_uniq_code(self):
        return self._hospital_uniq_code

    @hospital_uniq_code.setter
    def hospital_uniq_code(self, value):
        self._hospital_uniq_code = value
    @property
    def isv_code(self):
        return self._isv_code

    @isv_code.setter
    def isv_code(self, value):
        self._isv_code = value
    @property
    def isv_display_first_page_url(self):
        return self._isv_display_first_page_url

    @isv_display_first_page_url.setter
    def isv_display_first_page_url(self, value):
        self._isv_display_first_page_url = value
    @property
    def isv_display_logo(self):
        return self._isv_display_logo

    @isv_display_logo.setter
    def isv_display_logo(self, value):
        self._isv_display_logo = value
    @property
    def isv_display_name(self):
        return self._isv_display_name

    @isv_display_name.setter
    def isv_display_name(self, value):
        self._isv_display_name = value
    @property
    def isv_name(self):
        return self._isv_name

    @isv_name.setter
    def isv_name(self, value):
        self._isv_name = value
    @property
    def jump_url(self):
        return self._jump_url

    @jump_url.setter
    def jump_url(self, value):
        self._jump_url = value
    @property
    def main_open_id(self):
        return self._main_open_id

    @main_open_id.setter
    def main_open_id(self, value):
        self._main_open_id = value
    @property
    def main_user_id(self):
        return self._main_user_id

    @main_user_id.setter
    def main_user_id(self, value):
        self._main_user_id = value
    @property
    def new_order_status(self):
        return self._new_order_status

    @new_order_status.setter
    def new_order_status(self, value):
        self._new_order_status = value
    @property
    def new_order_status_desc(self):
        return self._new_order_status_desc

    @new_order_status_desc.setter
    def new_order_status_desc(self, value):
        self._new_order_status_desc = value
    @property
    def number_seq_no(self):
        return self._number_seq_no

    @number_seq_no.setter
    def number_seq_no(self, value):
        self._number_seq_no = value
    @property
    def order_detail_url(self):
        return self._order_detail_url

    @order_detail_url.setter
    def order_detail_url(self, value):
        self._order_detail_url = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, value):
        self._patient_id = value
    @property
    def patient_name(self):
        return self._patient_name

    @patient_name.setter
    def patient_name(self, value):
        self._patient_name = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def pickup_end_time(self):
        return self._pickup_end_time

    @pickup_end_time.setter
    def pickup_end_time(self, value):
        self._pickup_end_time = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def register_date(self):
        return self._register_date

    @register_date.setter
    def register_date(self, value):
        self._register_date = value
    @property
    def register_evaluate(self):
        return self._register_evaluate

    @register_evaluate.setter
    def register_evaluate(self, value):
        self._register_evaluate = value
    @property
    def register_fee(self):
        return self._register_fee

    @register_fee.setter
    def register_fee(self, value):
        self._register_fee = value
    @property
    def register_hint_msg(self):
        return self._register_hint_msg

    @register_hint_msg.setter
    def register_hint_msg(self, value):
        self._register_hint_msg = value
    @property
    def register_hos_detail_loc(self):
        return self._register_hos_detail_loc

    @register_hos_detail_loc.setter
    def register_hos_detail_loc(self, value):
        self._register_hos_detail_loc = value
    @property
    def register_line_number(self):
        return self._register_line_number

    @register_line_number.setter
    def register_line_number(self, value):
        self._register_line_number = value
    @property
    def register_ticket(self):
        return self._register_ticket

    @register_ticket.setter
    def register_ticket(self, value):
        self._register_ticket = value
    @property
    def register_time(self):
        return self._register_time

    @register_time.setter
    def register_time(self, value):
        self._register_time = value
    @property
    def register_type(self):
        return self._register_type

    @register_type.setter
    def register_type(self, value):
        self._register_type = value
    @property
    def register_type_desc(self):
        return self._register_type_desc

    @register_type_desc.setter
    def register_type_desc(self, value):
        self._register_type_desc = value
    @property
    def reimburse_claim_status(self):
        return self._reimburse_claim_status

    @reimburse_claim_status.setter
    def reimburse_claim_status(self, value):
        self._reimburse_claim_status = value
    @property
    def reimburse_text(self):
        return self._reimburse_text

    @reimburse_text.setter
    def reimburse_text(self, value):
        self._reimburse_text = value
    @property
    def reimburse_url(self):
        return self._reimburse_url

    @reimburse_url.setter
    def reimburse_url(self, value):
        self._reimburse_url = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def scm_info(self):
        return self._scm_info

    @scm_info.setter
    def scm_info(self, value):
        self._scm_info = value
    @property
    def status_reason(self):
        return self._status_reason

    @status_reason.setter
    def status_reason(self, value):
        self._status_reason = value
    @property
    def support_refund(self):
        return self._support_refund

    @support_refund.setter
    def support_refund(self, value):
        self._support_refund = value
    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        if isinstance(value, list):
            self._tags = list()
            for i in value:
                self._tags.append(i)
    @property
    def treat_tips(self):
        return self._treat_tips

    @treat_tips.setter
    def treat_tips(self, value):
        if isinstance(value, TreatTips):
            self._treat_tips = value
        else:
            self._treat_tips = TreatTips.from_alipay_dict(value)
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value
    @property
    def univ_department_id(self):
        return self._univ_department_id

    @univ_department_id.setter
    def univ_department_id(self, value):
        self._univ_department_id = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value
    @property
    def visit_purpose(self):
        return self._visit_purpose

    @visit_purpose.setter
    def visit_purpose(self, value):
        self._visit_purpose = value
    @property
    def week_num(self):
        return self._week_num

    @week_num.setter
    def week_num(self, value):
        self._week_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.buss_type:
            if hasattr(self.buss_type, 'to_alipay_dict'):
                params['buss_type'] = self.buss_type.to_alipay_dict()
            else:
                params['buss_type'] = self.buss_type
        if self.button_list:
            if isinstance(self.button_list, list):
                for i in range(0, len(self.button_list)):
                    element = self.button_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.button_list[i] = element.to_alipay_dict()
            if hasattr(self.button_list, 'to_alipay_dict'):
                params['button_list'] = self.button_list.to_alipay_dict()
            else:
                params['button_list'] = self.button_list
        if self.campus_name:
            if hasattr(self.campus_name, 'to_alipay_dict'):
                params['campus_name'] = self.campus_name.to_alipay_dict()
            else:
                params['campus_name'] = self.campus_name
        if self.cancel_reason:
            if hasattr(self.cancel_reason, 'to_alipay_dict'):
                params['cancel_reason'] = self.cancel_reason.to_alipay_dict()
            else:
                params['cancel_reason'] = self.cancel_reason
        if self.cancel_time:
            if hasattr(self.cancel_time, 'to_alipay_dict'):
                params['cancel_time'] = self.cancel_time.to_alipay_dict()
            else:
                params['cancel_time'] = self.cancel_time
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.department_id:
            if hasattr(self.department_id, 'to_alipay_dict'):
                params['department_id'] = self.department_id.to_alipay_dict()
            else:
                params['department_id'] = self.department_id
        if self.department_name:
            if hasattr(self.department_name, 'to_alipay_dict'):
                params['department_name'] = self.department_name.to_alipay_dict()
            else:
                params['department_name'] = self.department_name
        if self.disease_description:
            if hasattr(self.disease_description, 'to_alipay_dict'):
                params['disease_description'] = self.disease_description.to_alipay_dict()
            else:
                params['disease_description'] = self.disease_description
        if self.disease_image_item_list:
            if isinstance(self.disease_image_item_list, list):
                for i in range(0, len(self.disease_image_item_list)):
                    element = self.disease_image_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.disease_image_item_list[i] = element.to_alipay_dict()
            if hasattr(self.disease_image_item_list, 'to_alipay_dict'):
                params['disease_image_item_list'] = self.disease_image_item_list.to_alipay_dict()
            else:
                params['disease_image_item_list'] = self.disease_image_item_list
        if self.disease_name:
            if hasattr(self.disease_name, 'to_alipay_dict'):
                params['disease_name'] = self.disease_name.to_alipay_dict()
            else:
                params['disease_name'] = self.disease_name
        if self.doctor_id:
            if hasattr(self.doctor_id, 'to_alipay_dict'):
                params['doctor_id'] = self.doctor_id.to_alipay_dict()
            else:
                params['doctor_id'] = self.doctor_id
        if self.doctor_inner_id:
            if hasattr(self.doctor_inner_id, 'to_alipay_dict'):
                params['doctor_inner_id'] = self.doctor_inner_id.to_alipay_dict()
            else:
                params['doctor_inner_id'] = self.doctor_inner_id
        if self.doctor_logo:
            if hasattr(self.doctor_logo, 'to_alipay_dict'):
                params['doctor_logo'] = self.doctor_logo.to_alipay_dict()
            else:
                params['doctor_logo'] = self.doctor_logo
        if self.doctor_name:
            if hasattr(self.doctor_name, 'to_alipay_dict'):
                params['doctor_name'] = self.doctor_name.to_alipay_dict()
            else:
                params['doctor_name'] = self.doctor_name
        if self.doctor_title:
            if hasattr(self.doctor_title, 'to_alipay_dict'):
                params['doctor_title'] = self.doctor_title.to_alipay_dict()
            else:
                params['doctor_title'] = self.doctor_title
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.first_visit_with_doctor:
            if hasattr(self.first_visit_with_doctor, 'to_alipay_dict'):
                params['first_visit_with_doctor'] = self.first_visit_with_doctor.to_alipay_dict()
            else:
                params['first_visit_with_doctor'] = self.first_visit_with_doctor
        if self.hint_message:
            if hasattr(self.hint_message, 'to_alipay_dict'):
                params['hint_message'] = self.hint_message.to_alipay_dict()
            else:
                params['hint_message'] = self.hint_message
        if self.hos_institution_code:
            if hasattr(self.hos_institution_code, 'to_alipay_dict'):
                params['hos_institution_code'] = self.hos_institution_code.to_alipay_dict()
            else:
                params['hos_institution_code'] = self.hos_institution_code
        if self.hospital_grade:
            if hasattr(self.hospital_grade, 'to_alipay_dict'):
                params['hospital_grade'] = self.hospital_grade.to_alipay_dict()
            else:
                params['hospital_grade'] = self.hospital_grade
        if self.hospital_id:
            if hasattr(self.hospital_id, 'to_alipay_dict'):
                params['hospital_id'] = self.hospital_id.to_alipay_dict()
            else:
                params['hospital_id'] = self.hospital_id
        if self.hospital_logo:
            if hasattr(self.hospital_logo, 'to_alipay_dict'):
                params['hospital_logo'] = self.hospital_logo.to_alipay_dict()
            else:
                params['hospital_logo'] = self.hospital_logo
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.hospital_tel_number:
            if hasattr(self.hospital_tel_number, 'to_alipay_dict'):
                params['hospital_tel_number'] = self.hospital_tel_number.to_alipay_dict()
            else:
                params['hospital_tel_number'] = self.hospital_tel_number
        if self.hospital_uniq_code:
            if hasattr(self.hospital_uniq_code, 'to_alipay_dict'):
                params['hospital_uniq_code'] = self.hospital_uniq_code.to_alipay_dict()
            else:
                params['hospital_uniq_code'] = self.hospital_uniq_code
        if self.isv_code:
            if hasattr(self.isv_code, 'to_alipay_dict'):
                params['isv_code'] = self.isv_code.to_alipay_dict()
            else:
                params['isv_code'] = self.isv_code
        if self.isv_display_first_page_url:
            if hasattr(self.isv_display_first_page_url, 'to_alipay_dict'):
                params['isv_display_first_page_url'] = self.isv_display_first_page_url.to_alipay_dict()
            else:
                params['isv_display_first_page_url'] = self.isv_display_first_page_url
        if self.isv_display_logo:
            if hasattr(self.isv_display_logo, 'to_alipay_dict'):
                params['isv_display_logo'] = self.isv_display_logo.to_alipay_dict()
            else:
                params['isv_display_logo'] = self.isv_display_logo
        if self.isv_display_name:
            if hasattr(self.isv_display_name, 'to_alipay_dict'):
                params['isv_display_name'] = self.isv_display_name.to_alipay_dict()
            else:
                params['isv_display_name'] = self.isv_display_name
        if self.isv_name:
            if hasattr(self.isv_name, 'to_alipay_dict'):
                params['isv_name'] = self.isv_name.to_alipay_dict()
            else:
                params['isv_name'] = self.isv_name
        if self.jump_url:
            if hasattr(self.jump_url, 'to_alipay_dict'):
                params['jump_url'] = self.jump_url.to_alipay_dict()
            else:
                params['jump_url'] = self.jump_url
        if self.main_open_id:
            if hasattr(self.main_open_id, 'to_alipay_dict'):
                params['main_open_id'] = self.main_open_id.to_alipay_dict()
            else:
                params['main_open_id'] = self.main_open_id
        if self.main_user_id:
            if hasattr(self.main_user_id, 'to_alipay_dict'):
                params['main_user_id'] = self.main_user_id.to_alipay_dict()
            else:
                params['main_user_id'] = self.main_user_id
        if self.new_order_status:
            if hasattr(self.new_order_status, 'to_alipay_dict'):
                params['new_order_status'] = self.new_order_status.to_alipay_dict()
            else:
                params['new_order_status'] = self.new_order_status
        if self.new_order_status_desc:
            if hasattr(self.new_order_status_desc, 'to_alipay_dict'):
                params['new_order_status_desc'] = self.new_order_status_desc.to_alipay_dict()
            else:
                params['new_order_status_desc'] = self.new_order_status_desc
        if self.number_seq_no:
            if hasattr(self.number_seq_no, 'to_alipay_dict'):
                params['number_seq_no'] = self.number_seq_no.to_alipay_dict()
            else:
                params['number_seq_no'] = self.number_seq_no
        if self.order_detail_url:
            if hasattr(self.order_detail_url, 'to_alipay_dict'):
                params['order_detail_url'] = self.order_detail_url.to_alipay_dict()
            else:
                params['order_detail_url'] = self.order_detail_url
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.patient_id:
            if hasattr(self.patient_id, 'to_alipay_dict'):
                params['patient_id'] = self.patient_id.to_alipay_dict()
            else:
                params['patient_id'] = self.patient_id
        if self.patient_name:
            if hasattr(self.patient_name, 'to_alipay_dict'):
                params['patient_name'] = self.patient_name.to_alipay_dict()
            else:
                params['patient_name'] = self.patient_name
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.pickup_end_time:
            if hasattr(self.pickup_end_time, 'to_alipay_dict'):
                params['pickup_end_time'] = self.pickup_end_time.to_alipay_dict()
            else:
                params['pickup_end_time'] = self.pickup_end_time
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.register_date:
            if hasattr(self.register_date, 'to_alipay_dict'):
                params['register_date'] = self.register_date.to_alipay_dict()
            else:
                params['register_date'] = self.register_date
        if self.register_evaluate:
            if hasattr(self.register_evaluate, 'to_alipay_dict'):
                params['register_evaluate'] = self.register_evaluate.to_alipay_dict()
            else:
                params['register_evaluate'] = self.register_evaluate
        if self.register_fee:
            if hasattr(self.register_fee, 'to_alipay_dict'):
                params['register_fee'] = self.register_fee.to_alipay_dict()
            else:
                params['register_fee'] = self.register_fee
        if self.register_hint_msg:
            if hasattr(self.register_hint_msg, 'to_alipay_dict'):
                params['register_hint_msg'] = self.register_hint_msg.to_alipay_dict()
            else:
                params['register_hint_msg'] = self.register_hint_msg
        if self.register_hos_detail_loc:
            if hasattr(self.register_hos_detail_loc, 'to_alipay_dict'):
                params['register_hos_detail_loc'] = self.register_hos_detail_loc.to_alipay_dict()
            else:
                params['register_hos_detail_loc'] = self.register_hos_detail_loc
        if self.register_line_number:
            if hasattr(self.register_line_number, 'to_alipay_dict'):
                params['register_line_number'] = self.register_line_number.to_alipay_dict()
            else:
                params['register_line_number'] = self.register_line_number
        if self.register_ticket:
            if hasattr(self.register_ticket, 'to_alipay_dict'):
                params['register_ticket'] = self.register_ticket.to_alipay_dict()
            else:
                params['register_ticket'] = self.register_ticket
        if self.register_time:
            if hasattr(self.register_time, 'to_alipay_dict'):
                params['register_time'] = self.register_time.to_alipay_dict()
            else:
                params['register_time'] = self.register_time
        if self.register_type:
            if hasattr(self.register_type, 'to_alipay_dict'):
                params['register_type'] = self.register_type.to_alipay_dict()
            else:
                params['register_type'] = self.register_type
        if self.register_type_desc:
            if hasattr(self.register_type_desc, 'to_alipay_dict'):
                params['register_type_desc'] = self.register_type_desc.to_alipay_dict()
            else:
                params['register_type_desc'] = self.register_type_desc
        if self.reimburse_claim_status:
            if hasattr(self.reimburse_claim_status, 'to_alipay_dict'):
                params['reimburse_claim_status'] = self.reimburse_claim_status.to_alipay_dict()
            else:
                params['reimburse_claim_status'] = self.reimburse_claim_status
        if self.reimburse_text:
            if hasattr(self.reimburse_text, 'to_alipay_dict'):
                params['reimburse_text'] = self.reimburse_text.to_alipay_dict()
            else:
                params['reimburse_text'] = self.reimburse_text
        if self.reimburse_url:
            if hasattr(self.reimburse_url, 'to_alipay_dict'):
                params['reimburse_url'] = self.reimburse_url.to_alipay_dict()
            else:
                params['reimburse_url'] = self.reimburse_url
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.scm_info:
            if hasattr(self.scm_info, 'to_alipay_dict'):
                params['scm_info'] = self.scm_info.to_alipay_dict()
            else:
                params['scm_info'] = self.scm_info
        if self.status_reason:
            if hasattr(self.status_reason, 'to_alipay_dict'):
                params['status_reason'] = self.status_reason.to_alipay_dict()
            else:
                params['status_reason'] = self.status_reason
        if self.support_refund:
            if hasattr(self.support_refund, 'to_alipay_dict'):
                params['support_refund'] = self.support_refund.to_alipay_dict()
            else:
                params['support_refund'] = self.support_refund
        if self.tags:
            if isinstance(self.tags, list):
                for i in range(0, len(self.tags)):
                    element = self.tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tags[i] = element.to_alipay_dict()
            if hasattr(self.tags, 'to_alipay_dict'):
                params['tags'] = self.tags.to_alipay_dict()
            else:
                params['tags'] = self.tags
        if self.treat_tips:
            if hasattr(self.treat_tips, 'to_alipay_dict'):
                params['treat_tips'] = self.treat_tips.to_alipay_dict()
            else:
                params['treat_tips'] = self.treat_tips
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        if self.univ_department_id:
            if hasattr(self.univ_department_id, 'to_alipay_dict'):
                params['univ_department_id'] = self.univ_department_id.to_alipay_dict()
            else:
                params['univ_department_id'] = self.univ_department_id
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
        if self.visit_purpose:
            if hasattr(self.visit_purpose, 'to_alipay_dict'):
                params['visit_purpose'] = self.visit_purpose.to_alipay_dict()
            else:
                params['visit_purpose'] = self.visit_purpose
        if self.week_num:
            if hasattr(self.week_num, 'to_alipay_dict'):
                params['week_num'] = self.week_num.to_alipay_dict()
            else:
                params['week_num'] = self.week_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalRegisterOrderInfo()
        if 'address' in d:
            o.address = d['address']
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'buss_type' in d:
            o.buss_type = d['buss_type']
        if 'button_list' in d:
            o.button_list = d['button_list']
        if 'campus_name' in d:
            o.campus_name = d['campus_name']
        if 'cancel_reason' in d:
            o.cancel_reason = d['cancel_reason']
        if 'cancel_time' in d:
            o.cancel_time = d['cancel_time']
        if 'channel' in d:
            o.channel = d['channel']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'date' in d:
            o.date = d['date']
        if 'department_id' in d:
            o.department_id = d['department_id']
        if 'department_name' in d:
            o.department_name = d['department_name']
        if 'disease_description' in d:
            o.disease_description = d['disease_description']
        if 'disease_image_item_list' in d:
            o.disease_image_item_list = d['disease_image_item_list']
        if 'disease_name' in d:
            o.disease_name = d['disease_name']
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'doctor_inner_id' in d:
            o.doctor_inner_id = d['doctor_inner_id']
        if 'doctor_logo' in d:
            o.doctor_logo = d['doctor_logo']
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        if 'doctor_title' in d:
            o.doctor_title = d['doctor_title']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'first_visit_with_doctor' in d:
            o.first_visit_with_doctor = d['first_visit_with_doctor']
        if 'hint_message' in d:
            o.hint_message = d['hint_message']
        if 'hos_institution_code' in d:
            o.hos_institution_code = d['hos_institution_code']
        if 'hospital_grade' in d:
            o.hospital_grade = d['hospital_grade']
        if 'hospital_id' in d:
            o.hospital_id = d['hospital_id']
        if 'hospital_logo' in d:
            o.hospital_logo = d['hospital_logo']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'hospital_tel_number' in d:
            o.hospital_tel_number = d['hospital_tel_number']
        if 'hospital_uniq_code' in d:
            o.hospital_uniq_code = d['hospital_uniq_code']
        if 'isv_code' in d:
            o.isv_code = d['isv_code']
        if 'isv_display_first_page_url' in d:
            o.isv_display_first_page_url = d['isv_display_first_page_url']
        if 'isv_display_logo' in d:
            o.isv_display_logo = d['isv_display_logo']
        if 'isv_display_name' in d:
            o.isv_display_name = d['isv_display_name']
        if 'isv_name' in d:
            o.isv_name = d['isv_name']
        if 'jump_url' in d:
            o.jump_url = d['jump_url']
        if 'main_open_id' in d:
            o.main_open_id = d['main_open_id']
        if 'main_user_id' in d:
            o.main_user_id = d['main_user_id']
        if 'new_order_status' in d:
            o.new_order_status = d['new_order_status']
        if 'new_order_status_desc' in d:
            o.new_order_status_desc = d['new_order_status_desc']
        if 'number_seq_no' in d:
            o.number_seq_no = d['number_seq_no']
        if 'order_detail_url' in d:
            o.order_detail_url = d['order_detail_url']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'patient_id' in d:
            o.patient_id = d['patient_id']
        if 'patient_name' in d:
            o.patient_name = d['patient_name']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'period' in d:
            o.period = d['period']
        if 'pickup_end_time' in d:
            o.pickup_end_time = d['pickup_end_time']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'register_date' in d:
            o.register_date = d['register_date']
        if 'register_evaluate' in d:
            o.register_evaluate = d['register_evaluate']
        if 'register_fee' in d:
            o.register_fee = d['register_fee']
        if 'register_hint_msg' in d:
            o.register_hint_msg = d['register_hint_msg']
        if 'register_hos_detail_loc' in d:
            o.register_hos_detail_loc = d['register_hos_detail_loc']
        if 'register_line_number' in d:
            o.register_line_number = d['register_line_number']
        if 'register_ticket' in d:
            o.register_ticket = d['register_ticket']
        if 'register_time' in d:
            o.register_time = d['register_time']
        if 'register_type' in d:
            o.register_type = d['register_type']
        if 'register_type_desc' in d:
            o.register_type_desc = d['register_type_desc']
        if 'reimburse_claim_status' in d:
            o.reimburse_claim_status = d['reimburse_claim_status']
        if 'reimburse_text' in d:
            o.reimburse_text = d['reimburse_text']
        if 'reimburse_url' in d:
            o.reimburse_url = d['reimburse_url']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'scm_info' in d:
            o.scm_info = d['scm_info']
        if 'status_reason' in d:
            o.status_reason = d['status_reason']
        if 'support_refund' in d:
            o.support_refund = d['support_refund']
        if 'tags' in d:
            o.tags = d['tags']
        if 'treat_tips' in d:
            o.treat_tips = d['treat_tips']
        if 'unit' in d:
            o.unit = d['unit']
        if 'univ_department_id' in d:
            o.univ_department_id = d['univ_department_id']
        if 'update_time' in d:
            o.update_time = d['update_time']
        if 'visit_purpose' in d:
            o.visit_purpose = d['visit_purpose']
        if 'week_num' in d:
            o.week_num = d['week_num']
        return o


