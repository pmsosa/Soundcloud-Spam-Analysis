class ShowcaseController < ApplicationController

  def information

    uri =URI.parse("http://api.soundcloud.com/users/#{find_user_by_username(params[:id])}?client_id=02gUJC0hH2ct1EGOcYXQIzRFU91c72Ea")
    response = Net::HTTP.get_response(uri)
    @confidence_rate = 40
    @selected_image = if user_is_spam?
                        view_context.image_path('bot.jpg')
                      else
                        view_context.image_path('human.jpg')
                      end
    @user = JSON.parse response.body
  end

  private

  def find_user_by_username username
    uri = URI.parse "https://soundcloud.com/#{username}"
    response = Net::HTTP.get_response(uri)
    id = response.body.inspect.match(/soundcloud:\/\/users:(\d+)/).captures

    id.first.to_i
  end

  def user_is_spam?
    false
  end
end
