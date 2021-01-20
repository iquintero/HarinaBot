import discord
import os
from player import YTDLSource

#text_channel_id = 346777875363659776
text_channel_id = 176155607865360384
dota_basshunter = 'https://www.youtube.com/watch?v=aTJncWndUB8'

users = {
    'Mr.Roboto#5572': 'Mr Roboto',
    'Frankie#9021': 'el Feeder del Frankie',
    'kkwatito#6706': 'Mimosa Chan',
    'Shax#3753': 'El Caballero',
    'RokloMX#9669': 'Orflo',
    'hics#0985': 'Obachan',
    'Quintana#8403': 'Kingtana (smurf)',
}


class HarinaClient(discord.Client):

  voiceChannel = None
  isPlaying = False

  async def on_ready(self):
      print('We have logged in as {0.user}'.format(client))

  async def on_message(self, message):
      print(message.channel)
      if message.author == client.user:
          return

      if message.content.startswith('$hello'):
          await message.channel.send('Hello!')


  async def on_voice_state_update(self, member, before, after):
      if before.channel is None and after.channel is not None:
          key = member.name + "#" + member.discriminator
          channel = await client.fetch_channel(text_channel_id)

          if (channel and key in users):
            await channel.send(':eyes: Ya llego ' + users[key])
            if self.voiceChannel is None:
              self.voiceChannel = await after.channel.connect()
              if not self.isPlaying:
                player = await YTDLSource.from_url(dota_basshunter)
                self.voiceChannel.play(player, after= lambda e: self._after_playing(e))
                self.isPlaying = True
            else:
              print('Already playing')

  def _after_playing(self, e):
    if e:
      print('Player error: %s' % e)
    self.isPlaying = False



if __name__ == "__main__":
  client = HarinaClient()
  client.run(os.getenv('TOKEN'))
